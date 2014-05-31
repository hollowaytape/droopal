'use strict';


// Declare app level module which depends on filters, and services
angular.module('droopal', [
  'ngRoute',
  'leaflet-directive',
  'highcharts-ng'
])

    .config(['$routeProvider', function ($routeProvider) {
      $routeProvider.when('/trees', {templateUrl: 'static/trees/trees.html', controller: 'TreesCtrl'});
      $routeProvider.when('/tree-details/:id', {templateUrl: 'static/tree-details/tree-details.html', controller: 'TreeDetailsCtrl'});
      $routeProvider.otherwise({redirectTo: '/trees'});
    }]);
