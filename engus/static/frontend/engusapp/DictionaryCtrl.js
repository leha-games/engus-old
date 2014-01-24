angular.module('engusApp').controller('DictionaryCtrl', 
    ['$scope', '$state', '$stateParams', 'WordFlatList',
    function($scope, $state, $stateParams, WordFlatList) {
        this.dictionary = WordFlatList.data;
        this.search = function(word) {
            var self = this;
            this.searching = true;
            $state.go('base.dictionary.word', { word: this.word }).then(function() {
                self.word = '';
                self.searching = false;
            });
        };
        this.startsWith = function(expected, actual) {
            return expected.substr(0, actual.length).toLowerCase() == actual.toLowerCase();
        }
        this.triggerSubmit = function() {
            $scope.$broadcast('submitForm');
        };
    }
]);

angular.module('engusApp').controller('DictionaryWordCtrl',
    ['$stateParams', 'Profile', 'Word', 'WordExamples', 'Cards', 'CardService',
    function($stateParams, Profile, Word, WordExamples, Cards, CardService) {
        var self = this;
        this.rawWord = $stateParams.word;
        this.word = Word;
        this.profile = Profile;
        this.loading = true;
        this.cardsLoading = true;
        this.wordNotFound = false;
        this.examples = WordExamples;
        this.card = undefined;
        Cards.$promise.then(function(cards) {
            self.cardsLoading = false;
            if (cards.length > 0) {
                self.card = cards[0];
            };
        });
        Word.$promise.then(
            function(word) {
                self.loading = false;
                self.word.definitionGroups = _.groupBy(word.definition_set, 'part_of_speach');
            },
            function() {
                self.loading = false;
                self.wordNotFound = true;
            }
        );
        this.switchCard = function() {
            if (this.card === undefined) {
                this.card = new CardService({ word: self.word.word });
                this.card.$save();
            } else {
                this.card.$remove();
                this.card = undefined;
            };
        };
                
    }
]);

angular.module('engusApp').controller('CardsCtrl',
    ['Cards', 
    function(Cards, $location) {
        var self = this;
        this.loading = true;
        this.cards = Cards;
        this.statusFilter = 0;
        Cards.$promise.then(function() {
            self.loading = false;
        });
        this.saveCard =  function(card) {
            card.$update();
        };
        this.changeStatusFilter = function(newStatus) {
            $location.search({'status': newStatus});
        };
    }
]);

angular.module('engusApp').controller('HomeCtrl',
    ['Profile', 
    function(Profile) {
        var self = this;
        this.profile = Profile;
        this.saveProfile = function() {
            self.profile.$update();
        };
    }
]);

angular.module('engusApp').controller('CardsLearningCtrl',
    ['Cards', 'Profile', '$filter', '$stateParams', 'CardService', 'WordService', 'ExampleService',
    function(Cards, Profile, $filter, $stateParams, CardService, WordService, ExampleService) {
        var self = this;
        this.loading = true;
        this.profile = Profile;
        this.statusFilter = $stateParams.status;

        var getFullCard = function(card) {
            var word = WordService.get({ word: card.word }, function() {
                    word.definitionGroups = _.groupBy(word.definition_set, 'part_of_speach');
                }),
                examples = ExampleService.query({ 'definition__word': card.word }, function() {
                    examples.random = getRandomElement(examples);
                });
            return {
                card: card,
                word: word,
                examples: examples,
                showDefinitions: false,
            };
        };

        var getNextCard = function(card) {
            return getNextElement(self.orderedCards, card);
        };

        var getNextElement = function(array, element) {
            var indexOfElement = array.indexOf(element),
                nextElement = undefined;
            if (indexOfElement < (array.length - 1)) {
                nextElement = array[indexOfElement + 1];
            } else {
                nextElement = array[0];
            }
            return nextElement;
        };

        var getRandomElement = function(array) {
            return array[Math.floor(Math.random() * array.length)];
        };


        Cards.$promise.then(
            function(cards) {
                self.loading = false;
                var filteredCards = $filter('filter')(Cards, {'status': self.statusFilter});
                self.orderedCards = $filter('orderBy')(filteredCards, ['level', '-created']);
                var firstCard = self.orderedCards[0];
                self.current = getFullCard(firstCard);
                self.next = getFullCard(getNextCard(firstCard));
            },
            function() {

            }
        );
        this.switchCard = function(state) {
            switch (state) {
                case 'good':
                    this.current.card.level += 1;
                    this.current.card.$update();
                    break;
                case 'forget':
                    this.current.card.level = 0;
                    this.current.card.$update();
                    break;
            }
            this.current = this.next;
            this.next = getFullCard(getNextCard(this.current.card));
        };
    }
]);

angular.module('engusApp').factory('CardService', 
    ['$resource',
    function($resource) {
        return $resource('/cards/cards/:id', {id: '@id'}, 
            {
                'update': { method: 'PUT' }
            });
    }
]);

angular.module('engusApp').factory('WordService', 
    ['$resource',
    function($resource) {
        return $resource('/dictionary/words/:word', {word: '@word'});
    }
]);

angular.module('engusApp').factory('ExampleService', 
    ['$resource',
    function($resource) {
        return $resource('/dictionary/examples/:id', {id: '@id'});
    }
]);

angular.module('engusApp').factory('ProfileService', 
    ['$resource',
    function($resource) {
        return $resource('/accounts/profiles/:id', {id: '@id'}, {'update': {method: 'PUT'}});
    }
]);

angular.module('engusApp').directive('blurOnSubmit', function() {
    return function(scope, element, attrs) {
        var formOfElement = angular.element(element[0].form);
        formOfElement.bind('submit', function() {
            element[0].blur();
        });
    };
});

angular.module('engusApp').directive('blurWithTimeout', 
    ['$timeout', function($timeout) {
        return function(scope, element, attrs) {
            element.on('blur', function(event) {
                $timeout(function() { scope.$eval(attrs.blurWithTimeout) }, 50);
            });
        };
    }]
);

angular.module('engusApp').filter('markWord', ['$sce', function($sce) {
    return function(input, word) {
        var out;
        var re = new RegExp('((?:' + word + ')\\w*)', 'g');
        out = input.replace(re, '<b class="bold">$1</b>');
        return $sce.trustAsHtml(out);
    }
}]);

angular.module('engusApp').filter('groupBy', function() {
    return function(input, by) {
        return _.groupBy(input, by);
    }
});

angular.module('engusApp').filter('declOfNum', function() {
    return function(number, titles) {
        var cases = [2, 0, 1, 1, 1, 2];
        return titles[ (number % 100 > 4 && number % 100 < 20) ? 2 : cases[(number % 10 < 5) ? number % 10 : 5] ];
    }
});

angular.module('engusApp').filter('mueller', ['$sce', function($sce) {
    return function(input) {
        var out;
        out = input.replace(/(\S{1})>/g, 
            '<span class="dictionary__mueller-numbers4">$1)</span>'); // fourth level. a> б> в>
        out = out.replace(/(\d{1,3})\)(.*)/g, 
            '<div class="dictionary__mueller-level3"><span class="dictionary__mueller-numbers3">$1)</span>$2</div>'); // third level. 1) 2) 3)
        out = out.replace(/(\d{1,3}\.)(.*)\n/g, 
            '<div class="dictionary__mueller-level2"><span class="dictionary__mueller-numbers2">$1</span>$2</div>'); // second level. 1. 2. 3.
        out = out.replace(/(?=[IVX])(X{0,3}I{0,3}|X{0,2}VI{0,3}|X{0,2}I?[VX])\)/g, 
            '<span class="dictionary__mueller-numbers1">$1.</span>'); // first level. I) II) III)
        return $sce.trustAsHtml(out); 
    }
}]);

angular.module('engusApp').directive('transcription', function() {
    return {
        restrict: 'A',
        replace: true,
        templateUrl: 'templates/directives/transcription.html',
        link: function(scope, element, attrs) {
            scope.$watch(attrs.transcription, function(transcription) {
                scope.transcription = '[' + transcription + ']';
            });
            scope.$watch(attrs.audioSrc, function(audioSrc) {
                scope.audiosrc = audioSrc;
            });
            scope.playTranscription = function() {
                if (scope.audiosrc) {
                    element.find('audio')[0].play();
                };
            };
        }
    }
});

angular.module('engusApp').directive('submitOn', function() {
    return function(scope, element, attrs) {
        scope.$on(attrs.submitOn, function() {
            setTimeout(function() {
                element.triggerHandler('submit');
            });
        });
    };
});
