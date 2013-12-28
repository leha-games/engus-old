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
    ['Word', 'CardList', 'CardService', 'Restangular',
    function(Word, CardList, CardService, Restangular) {
        var word = this.word = Word.data;
        word.definitionsGroups = _.groupBy(word.definition_set, 'part_of_speach');
        this.card = _.find(CardList, function(card) {
            return card.word === word.id;
        });
        this.switchCard = function() {
            if (this.card === undefined) {
                this.card = new CardService({ word: word.id });
                this.card.$save();
            } else {
                var self = this;
                this.card.$remove();
                this.card = undefined;
            };
        };
                
    }
]);

angular.module('engusApp').factory('CardService', 
    ['$resource',
    function($resource) {
        return $resource('/cards/cards/:id', {id: '@id'});
    }
]);

angular.module('engusApp').factory('WordService', 
    ['$resource',
    function($resource) {
        return $resource('/dictionary/:word', {word: '@word'});
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
