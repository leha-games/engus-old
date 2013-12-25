angular.module('engusApp').controller('DictionaryCtrl', 
    ['$scope', '$state', '$stateParams', 'Dictionary',
    function($scope, $state, $stateParams, Dictionary) {
        this.dictionary = Dictionary.data;
        this.search = function(word) {
            $state.go('dictionary.word', { word: this.word });
            this.word = '';
        };
        this.startsWith = function(expected, actual) {
            return expected.substr(0, actual.length).toLowerCase() == actual.toLowerCase();
        }
    }
]);
angular.module('engusApp').controller('DictionaryWordCtrl',
    ['DictionaryWord',
    function(DictionaryWord) {
        this.word = DictionaryWord.data;
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
angular.module('engusApp').filter('mueller', function($sce) {
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
});

