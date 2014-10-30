angular.module('engusApp', ['ngResource', 'ui.router', 'ngTouch', 'infinite-scroll'])
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
                    }], 
                    Profile: ['ProfileService', function(ProfileService) {
                        return ProfileService.query().$promise.then(function(profiles) {
                            return profiles[0];
                        });
                    }],
                    Cards: ['CardService', function(CardService) {
                        return CardService.resource.query();
                    }]
                }
            })
            .state('base.dictionary', {
                url: 'dictionary/',
                templateUrl: 'templates/base.dictionary.html',
                controller: 'DictionaryCtrl as dict'
            })
            .state('base.dictionary.word', {
                url: '{word:[^/]+}/',
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
                        return CardService.resource.query({ 'word': $stateParams.word });
                    }]
                }
            })
            .state('base.profile', {
                url: 'profile/',
                templateUrl: 'templates/base.profile.html',
                controller: 'ProfileCtrl as ProfileCtrl'
            })
            .state('base.profile.statistics', {
                url: 'statistics/',
                templateUrl: 'templates/base.profile.statistics.html',
                controller: 'ProfileStatisticsCtrl as ProfileStatisticsCtrl'
            })
            .state('base.cards', {
                url: 'cards/',
                abstract: true,
                templateUrl: 'templates/base.cards.html',
                controller: 'CardsCtrl as CardsCtrl'
            })
            .state('base.cards.new', {
                url: 'new/',
                templateUrl: 'templates/base.cards.new.html'
            })
            .state('base.cards.done', {
                url: 'done/',
                templateUrl: 'templates/base.cards.done.html'
            })
            .state('base.cards.new.learn', {
                url: 'learn/',
                views: {
                    '@base': {
                        templateUrl: 'templates/base.cards.learning.html',
                        controller: 'LearningNewCardsCtrl as CardsLearningCtrl'
                    }
                }
            })
            .state('base.cards.done.repeat', {
                url: 'repeat/',
                views: {
                    '@base': {
                        templateUrl: 'templates/base.cards.learning.html',
                        controller: 'RepeatDoneCardsCtrl as CardsLearningCtrl'
                    }
                }
            });
    }
])
.run(['$rootScope', '$state', '$stateParams', '$location',
    function($rootScope, $state, $stateParams, $location) {
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;

        // Yandex.Metrica hit on location change success
        $rootScope.$on('$locationChangeSuccess', function() {
            var yaCounter23664607 = window.yaCounter23664607 || undefined;
            if (yaCounter23664607) {
                yaCounter23664607.hit($location.$$absUrl);
            }
        });
    }
]);
