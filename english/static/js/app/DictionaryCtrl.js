angular.module('engusApp').controller('DictionaryCtrl', 
    ['$scope', '$state', '$stateParams', 'Dictionary',
    function($scope, $state, $stateParams, Dictionary) {
        this.dictionary = Dictionary.data;
        this.search = function(word) {
            $state.go('base.dictionary.word', { word: this.word });
            this.word = '';
        };
        this.startsWith = function(expected, actual) {
            return expected.substr(0, actual.length).toLowerCase() == actual.toLowerCase();
        }
    }
]);
angular.module('engusApp').controller('DictionaryWordCtrl',
    ['Word', 'CardService',
    function(Word, CardService) {
        var word = this.word = Word;
        word.definitionsGroups = _.groupBy(word.definition_set, 'part_of_speach');
        this.card = function() {
            return CardService.getCard(word.id);
        };
        this.switchCard = function() {
            return CardService.switchCardForWord(this.card(), this.word.id);
        };
    }
]);
angular.module('engusApp').service('CardService', ['Restangular', function(Restangular) {
    var cards;
    this.cards = cards;
    this.getCardList = function() {
        return Restangular.one('cards').getList('cards').then(function(data) { 
            cards = data; 
        });
    };
    this.getCard = function(wordId) {
        var card = _.find(cards, function(card) {
            return card.word === wordId;
        });
        return card;
    };
    this.removeCard = function(card) {
        card.remove().then(function(data) { 
            cards.splice(cards.indexOf(card), 1);
        });
    };
    this.addCard = function(wordId) {
        cards.post({ word: wordId }).then(function(card) { 
            cards.push(card);
        });
    };
    this.switchCardForWord = function(card, wordId) {
        if (card === undefined) {
            this.addCard(wordId);
        } else {
            this.removeCard(card);
        }
    };
}]);
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
angular.module('engusApp').filter('mueller', ['$sce', function($sce) {
    return function(input) {
        var out;
        out = input.replace(/(\S{1})>/g, 
            '<span class="dictionary__muellerdef-numbers4">$1)</span>'); // fourth level. a> б> в>
        out = out.replace(/(\d{1,3})\)(.*)/g, 
            '<div class="dictionary__muellerdef-level3"><span class="dictionary__muellerdef-numbers3">$1)</span>$2</div>'); // third level. 1) 2) 3)
        out = out.replace(/(\d{1,3}\.)(.*)\n/g, 
            '<div class="dictionary__muellerdef-level2"><span class="dictionary__muellerdef-numbers2">$1</span>$2</div>'); // second level. 1. 2. 3.
        out = out.replace(/(?=[IVX])(X{0,3}I{0,3}|X{0,2}VI{0,3}|X{0,2}I?[VX])\)/g, 
            '<span class="dictionary__muellerdef-numbers1">$1.</span>'); // first level. I) II) III)
        return $sce.trustAsHtml(out); 
    }
}]);
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
        template: 
            '<div class="dictionary__headword-transcription" ng-mouseenter="transcriptionHover = true" ng-mouseleave="transcriptionHover = false">' +
                '<span>' +
                    '<i class="fa fa-volume-up dictionary__headword-transcription-audio" ng-class="{ hover: transcriptionHover }"></i>' +
                    '<audio id="transcription-audio" preload="auto">' +
                        '<source type="audio/mpeg">' +
                    '</audio>' +
                '</span>' +
            '</div>',
        link: function(scope, element, attrs) {
            var audioSrc = attrs.audioSrc,
                transcription = attrs.transcription,
                soundElement = element.children(),
                audioElements = soundElement.find('audio');
            if (transcription) {
                element.prepend('[' + transcription + ']');
                if (audioSrc) {
                    var sourceElement = audioElements.find('source')[0];
                    sourceElement.src = audioSrc;
                    element.bind('click', function() {
                        audioElements[0].play()
                    });
                    element.addClass('with-audio');
                } else {
                    soundElement.remove();
                };
            } else {
                element.remove();
            };
        }
    }
});
