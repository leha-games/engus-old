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
    ['$sce', 'DictionaryWord',
    function($sce, DictionaryWord) {
        this.worddef = $sce.trustAsHtml(DictionaryWord.data)
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


