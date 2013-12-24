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
        this.word = DictionaryWord.data;
        console.log(this.word);
    }
]);


