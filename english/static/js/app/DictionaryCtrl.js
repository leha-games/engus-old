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
    ['Word', 'WordExamples', 'Card', 'CardService',
    function(Word, WordExamples, Card, CardService) {
        var word = this.word = Word;
        if (word) {
            word.definitionsGroups = _.groupBy(word.definition_set, 'part_of_speach');
        };
        this.examples = WordExamples;
        this.card = Card;
        this.switchCard = function() {
            if (this.card === undefined) {
                this.card = new CardService({ word: word.word });
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
        var orderedCards = $filter('orderBy')(Cards, ['level', '-created']),
            firstCard = orderedCards[0];

        var getFullCard = function(card) {
            var word = WordService.get({ word: card.word }),
                examples = ExampleService.query({ 'definition__word': card.word }, function() {
                    examples.random = getRandomElement(examples);
                });
            return {
                card: card,
                word: word,
                examples: examples,
                showDefinitions: false
            };
        };

        var getNextCard = function(card) {
            return getNextElement(orderedCards, card);
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
        }

        this.current = getFullCard(firstCard);
        this.next = getFullCard(getNextCard(firstCard));
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
