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
    }
]);

angular.module('engusApp').controller('DictionaryWordCtrl',
    ['$stateParams', 'Word', 'WordExamples', 'Cards', 'CardService',
    function($stateParams, Word, WordExamples, Cards, CardService) {
        var self = this;
        this.rawWord = $stateParams.word;
        this.word = Word;
        this.loading = true;
        this.wordNotFound = false;
        this.examples = WordExamples;
        this.card = undefined;
        Cards.$promise.then(function(cards) {
            if (cards.length > 0) {
                self.card = cards[0];
            };
        });
        Word.$promise.then(
            function(word) {
                self.loading = false;
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
    function(Cards) {
        this.cards = Cards;
    }
]);

angular.module('engusApp').controller('CardsLearningCtrl',
    ['Cards', '$filter', 'CardService', 'WordService', 'ExampleService',
    function(Cards, $filter, CardService, WordService, ExampleService) {
        var self = this;
        this.loading = true;

        var getFullCard = function(card) {
            var word = WordService.get({ word: card.word }),
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
                self.orderedCards = $filter('orderBy')(Cards, ['level', '-created']);
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
        return $resource('/dictionary/examples/:id', {word: '@id'});
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
    return _.memoize(function(input, by) {
        return _.groupBy(input, by);
    });
});

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
