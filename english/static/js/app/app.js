angular.module('engusApp', ['restangular', 'ui.router'])
.config(['$httpProvider', '$locationProvider', '$stateProvider', '$urlRouterProvider',
    function($httpProvider, $locationProvider, $stateProvider, $urlRouterProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $urlRouterProvider.otherwise('/dictionary');

        $stateProvider
            .state('base', {
                abstract: true,
                templateUrl: '/static/js/app/templates/base.html',
                resolve: {
                    Cards: ['CardService', function(CardService) {
                        return CardService.getCardList();
                    }]
                }
            })
            .state('base.dictionary', {
                url: '/dictionary',
                templateUrl: '/static/js/app/templates/base.dictionary.html',
                controller: 'DictionaryCtrl as dict',
                resolve: {
                    Dictionary: function($http) {
                        return $http.get('/dictionary/');
                    }
                }
            })
            .state('base.dictionary.word', {
                url: '/:word',
                templateUrl: '/static/js/app/templates/base.dictionary.word.html',
                controller: 'DictionaryWordCtrl as WordCtrl',
                resolve: {
                    Word: ['Restangular', '$stateParams', function(Restangular, $stateParams) {
                        return Restangular.one('dictionary', $stateParams.word).get();
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
