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
            return expected.substr(0, actual.length).toLowerCase() === actual.toLowerCase();
        };
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
        var word = this.word = Word;
        this.profile = Profile;
        this.wordNotFound = false;
        this.examples = WordExamples;
        var cards = Cards;
        var getWordCard = this.getWordCard = function () {
            var wordCard = undefined;
            for (var i = 0; i < cards.length; i++) {
                if (cards[i].word === word.word) {
                    wordCard = cards[i];
                }
            }
            return wordCard;
        };
        this.isWordInCards = function() {
            return !!(getWordCard());
        };
        Word.$promise.then(
            function(word) {
                self.word.definitionGroups = _.groupBy(word.definition_set, 'part_of_speach');
            },
            function() {
                self.wordNotFound = true;
            }
        );
        this.switchCard = function() {
            if (this.isWordInCards()) {
                CardService.removeCard(cards, getWordCard());
            } else {
                CardService.addCard(cards, self.word.word );
            }
        };
                
    }
]);

angular.module('engusApp').controller('ProfileCtrl',
    ['Profile',
    function(Profile) {
        var self = this;
        this.profile = Profile;
        this.saveProfile = function() {
            self.profile.$update();
        };
    }
]);

angular.module('engusApp').controller('ProfileStatisticsCtrl',
    ['Cards', 'CardService',
    function(Cards, CardService) {
        var self = this;
        this.profile = Cards;
        this.getLearnedCardsCount = function() {
            return CardService.getLearned(Cards).length
        };
        this.getNewCardsCount = function() {
            return CardService.getToLearn(Cards).length
        }
    }
]);

angular.module('engusApp').controller('CardsCtrl',
    ['Cards', 'Profile', '$filter', 'CardService',
    function(Cards, Profile, $filter, CardService) {
        var self = this;
        this.loading = true;
        var cards = this.cards = Cards;
        this.profile = Profile;
        this.newCardsLimitTo = 50;
        this.doneCardsLimitTo = 50;
        this.isFilterLearned = false;
        Cards.$promise.then(function() {
            self.loading = false;
        });
        this.saveCard = function(card) {
            card.$update();
        };
        this.removeCard = function(card) {
            CardService.removeCard(cards, card)
        };
        this.moveInLearned = function(card) {
            card.status = 'learned';
            card.$update();
        };
        this.moveInNew = function(card) {
            card.status = 'new';
            card.$update();
        };
        this.moveInKnown = function(card) {
            card.status = 'know';
            card.$update();
        };
        this.getToLearnLater = CardService.getToLearnLater;
        this.getToLearnNow = CardService.getToLearnNow;
        this.getLearned = CardService.getLearned;

        this.cardsToLearn = function() {
            CardService.getToLearnNow(Cards, Profile);
        };

        this.cardsToLearnLater = function() {
            CardService.getToLearnLater(Cards, Profile);
        };

    }
]);

angular.module('engusApp').controller('LearningNewCardsCtrl',
    ['Cards', 'CardService', 'Profile', '$scope',
    function(Cards, CardService, Profile, $scope) {

        var self = this;
        var cardsToLearn = undefined;
        var next = undefined;
        var current = undefined;

        Cards.$promise.then(function(cards) {
            cardsToLearn = CardService.getToLearnNow(Cards, Profile);
            current = CardService.getFullCard(cardsToLearn[0]);
            next = CardService.getFullCard(CardService.getNextCard(cardsToLearn, current.card));
        });

        this.updateCard = CardService.updateCard;
        this.profile = Profile;

        this.cardsToLearn = function() {
            return CardService.getToLearnNow(cardsToLearn, Profile);
        };

        this.current = function() {
            return current;
        };

        this.switchCard = function() {
            var cardsToLearn = this.cardsToLearn();
            if (next) {
                current = next;
            } else {
                current = CardService.getFullCard(cardsToLearn[0]);
            }
            next = CardService.getFullCard(CardService.getNextCard(cardsToLearn, current.card));
        };
    }
]);

angular.module('engusApp').controller('RepeatDoneCardsCtrl',
    ['Cards', 'CardService', 'Profile', '$scope',
    function(Cards, CardService, Profile, $scope) {

        var self = this;
        var cardsToLearn = undefined;
        var next = undefined;
        var current = undefined;

        Cards.$promise.then(function(cards) {
            cardsToLearn = CardService.getLearned(Cards, Profile);
            current = CardService.getFullCard(cardsToLearn[0]);
            next = CardService.getFullCard(CardService.getNextCard(cardsToLearn, current.card));
        });

        this.updateCard = CardService.updateCard;
        this.profile = Profile;

        this.cardsToLearn = function() {
            return CardService.getLearned(cardsToLearn, Profile);
        };

        this.current = function() {
            return current;
        };

        this.switchCard = function() {
            var cardsToLearn = this.cardsToLearn();
            if (next) {
                current = next;
            } else {
                current = CardService.getFullCard(cardsToLearn[0]);
            }
            next = CardService.getFullCard(CardService.getNextCard(cardsToLearn, current.card));
        };
    }
]);

angular.module('engusApp').factory('CardService', 
    ['$resource', '$filter', 'WordService', 'ExampleService',
    function($resource, $filter, WordService, ExampleService) {

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

        var Card = {};

        Card.resource = $resource('/cards/cards/:id', {id: '@id'}, { 'update': { method: 'PUT' } });

        Card.updateCard = function(card, mode) {
            switch (mode) {
                case 'good':
                    card.level += 1;
                    card.$update();
                    break;
                case 'get':
                    card.status = 'learned';
                    card.$update();
                    break;
                case 'forget':
                    card.status = 'new';
                    card.$update();
                    break;
            }
        };

        Card.removeCard = function(cards, card) {
            cards.splice(cards.indexOf(card), 1);
            card.$remove()
        };

        Card.addCard = function(cards, word) {
            var newCard = new Card.resource({ word: word });
            cards.push(newCard);
            newCard.$save(function(savedCard) {
//                cards.push(savedCard);
                newCard = savedCard;
            });
        };

        Card.getFullCard = function(card) {
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
                showDefinitions: false
            };
        };

        Card.getNextCard = function(cards, card) {
            return getNextElement(cards, card);
        };

        Card.getLearned = function(cards) {
            var learnedCards = $filter('filter')(cards, {status: 'learned'});
            learnedCards = $filter('orderBy')(learnedCards, '-when_learned');
            return learnedCards;
        };

        Card.getToLearn = function(cards) {
            var cardsToLearn = $filter('filter')(cards, {status: 'new'});
            cardsToLearn = $filter('orderBy')(cardsToLearn, 'created');
            return cardsToLearn;
        };

        Card.getToLearnNow = function(cards, profile) {
            var cardsToLearnNow = Card.getToLearn(cards);
            cardsToLearnNow = $filter('limitTo')(cardsToLearnNow, profile.learn_by);
            cardsToLearnNow = $filter('orderBy')(cardsToLearnNow, '-level');
            return cardsToLearnNow;
        };

        Card.getToLearnLater = function(cards, profile) {
            var cardsToLearnLater = Card.getToLearn(cards);
            cardsToLearnLater = $filter('startFrom')(cardsToLearnLater, profile.learn_by);
            cardsToLearnLater = $filter('orderBy')(cardsToLearnLater, '-level');
            return cardsToLearnLater;
        };

        return Card;
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

angular.module('engusApp').filter('startFrom', function() {
    return function(input, start) {
        start = +start; // parse to int
        return input.slice(start);
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
                }
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
