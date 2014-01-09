angular.module('engusApp', ['ngResource', 'ui.router'])
.config(['$resourceProvider', '$httpProvider', '$locationProvider', '$stateProvider', '$urlRouterProvider',
    function($resourceProvider, $httpProvider, $locationProvider, $stateProvider, $urlRouterProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $urlRouterProvider.otherwise('/dictionary/');

        $stateProvider
            .state('base', {
                url: '/',
                abstract: true,
                templateUrl: 'templates/base.html',
                resolve: {
                    WordFlatList: ['$http', function($http) {
                        return $http.get('/dictionary/words/flat/');
                    }]
                }
            })
            .state('base.dictionary', {
                url: 'dictionary/',
                templateUrl: 'templates/base.dictionary.html',
                controller: 'DictionaryCtrl as dict'
            })
            .state('base.dictionary.word', {
                url: ':word/',
                templateUrl: 'templates/base.dictionary.word.html',
                controller: 'DictionaryWordCtrl as WordCtrl',
                resolve: {
                    Word: ['$stateParams', 'WordService', function($stateParams, WordService) {
                        return WordService.get({ word: $stateParams.word }); 
                    }],
                    WordExamples: ['$stateParams', 'ExampleService', function($stateParams, ExampleService) {
                        return ExampleService.query({ 'definition__word': $stateParams.word });
                    }],
                    Card: ['$stateParams', 'CardService', function($stateParams, CardService) {
                        return CardService.query({ 'word': $stateParams.word });
                    }]
                }
            })
            .state('base.home', {
                url: 'home/',
                template: ''
            })
            .state('base.cards', {
                url: 'cards/',
                templateUrl: 'templates/base.cards.html',
                controller: 'CardsCtrl as CardsCtrl',
                resolve: {
                    Cards: ['CardService', function(CardService) {
                        return CardService.query();
                    }]
                }
            })
            .state('base.cards.learning', {
                url: 'learning/',
                templateUrl: 'templates/base.cards.learning.html',
                controller: 'CardsLearningCtrl as CardsLearningCtrl'
            });
    }
])
.run(['$rootScope', '$state', '$stateParams',
    function($rootScope, $state, $stateParams) {
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;
    }
]);
