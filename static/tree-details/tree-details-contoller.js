'use strict';

/* Controllers */

angular.module('droopal')
    .controller('TreeDetailsCtrl', ['$scope', '$routeParams', function ($scope, $routeParams) {

      $scope.treename = 'Tree #91';

      $scope.predictedRipeDate = new Date();

      $scope.lastPickedQty = 10;

      angular.extend($scope, {
        defaults: {
          scrollWheelZoom: false
        },
        center: {
          lat: 33.7550,
          lng: -84.3900,
          zoom: 16
        }
      });


      $scope.treeChartConfig = {
        //This is not a highcharts object. It just looks a little like one!
        options: {
          //This is the Main Highcharts chart config. Any Highchart options are valid here.
          //will be ovverriden by values specified below.
          chart: {
            type: 'spline'
          },
          tooltip: {
            style: {
              padding: 10,
              fontWeight: 'bold'
            }
          }
        },

        //The below properties are watched separately for changes.

        //Series object (optional) - a list of series using normal highcharts series options.
        series: [
          {
            name: 'Sensor Value',
            data: [
              [1396235138000, 1],
              [1398913538000, 2],
              [1401505539000, 3],
              [1404183938000, 4],
              [1406775938000, 3]
            ]
          }
        ],
        //Title configuration (optional)
        title: {
          text: 'Ripeness'
        },
        //Boolean to control showng loading status on chart (optional)
        loading: false,
        //Configuration for the xAxis (optional). Currently only one x axis can be dynamically controlled.
        //properties currentMin and currentMax provied 2-way binding to the chart's maximimum and minimum
        xAxis: {
          title: {text: 'values'},
          type: 'datetime'
        },
        yAxis: {
          plotLines: [
            {
              value: 3,
              color: 'green',
              dashStyle: 'shortdash',
              width: 2,
              label: {
                text: 'Ripeness Threshold'
              }
            }
          ]
        },
        //Whether to use HighStocks instead of HighCharts (optional). Defaults to false.
        useHighStocks: false
      };


    }])
;