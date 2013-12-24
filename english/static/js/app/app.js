angular.module('engusApp', ['restangular', 'ui.router'])
.config(['$httpProvider', '$locationProvider', '$stateProvider', '$urlRouterProvider',
    function($httpProvider, $locationProvider, $stateProvider, $urlRouterProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

        $urlRouterProvider.otherwise('/dictionary/');

        $stateProvider
            .state('dictionary', {
                url: '/dictionary/',
                templateUrl: '/static/js/app/templates/dictionary.html',
                controller: 'DictionaryCtrl as dict',
                resolve: {
                    Dictionary: function($http) {
                        return $http.get('/dictionary/');
                    }
                }
            })
            .state('dictionary.word', {
                url: ':word',
                templateUrl: '/static/js/app/templates/dictionary.word.html',
                controller: 'DictionaryWordCtrl as WordCtrl',
                resolve: {
                    DictionaryWord: function($http, $stateParams) {
                        return $http.get('/dictionary/' + $stateParams.word);
                    }
                }
            });
}]);
