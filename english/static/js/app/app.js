angular.module('engusApp', ['ngResource', 'restangular', 'ui.router'])
.config(['$resourceProvider', '$httpProvider', '$locationProvider', '$stateProvider', '$urlRouterProvider',
    function($resourceProvider, $httpProvider, $locationProvider, $stateProvider, $urlRouterProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $urlRouterProvider.otherwise('/dictionary');

        $stateProvider
            .state('base', {
                abstract: true,
                templateUrl: '/static/js/app/templates/base.html'
            })
            .state('base.dictionary', {
                url: '/dictionary',
                templateUrl: '/static/js/app/templates/base.dictionary.html',
                controller: 'DictionaryCtrl as dict',
                resolve: {
                    WordFlatList: ['$http', function($http) {
                        return $http.get('/dictionary/words/flat/');
                    }]
                }
            })
            .state('base.dictionary.word', {
                url: '/:word',
                templateUrl: '/static/js/app/templates/base.dictionary.word.html',
                controller: 'DictionaryWordCtrl as WordCtrl',
                resolve: {
                    Word: ['$http', '$stateParams', function($http, $stateParams) {
                        return $http.get('/dictionary/words/' + $stateParams.word); 
                    }],
                    CardList: ['CardService', function(CardService) {
                        return CardService.query().$promise;
                    }]
                }
            })
            .state('base.home', {
                url: '/home',
                template: ''
            })
            .state('base.cards', {
                url: '/cards',
                template: ''
            });
    }
])
.run(['$rootScope', '$state', '$stateParams',
    function($rootScope, $state, $stateParams) {
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;
    }
]);
