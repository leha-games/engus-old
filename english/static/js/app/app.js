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
                        return $http.get('/dictionary/').success(function(result) { return result.data });
                    }
                }
            })
            .state('dictionary.word', {
                url: ':word',
                templateUrl: '/static/js/app/templates/dictionary.word.html',
                controller: 'DictionaryWordCtrl as word',
                resolve: {
                    DictionaryWord: function($http, $stateParams) {
                        return $http.get('/dictionary/' + $stateParams.word).success(function(result) { return result.data });
                    }
                }
            });
}]);
