'use strict';

/* Controllers */

angular.module('droopal')
    .controller('TreeDetailsCtrl', ['$scope', '$routeParams', '$http', 'leafletData', function ($scope, $routeParams,$http, leafletData) {


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


      $http({
        url: '/trees/'+$routeParams.id
      }).success(function (data) {

        var value = data.items[0];
        $scope.center.lat = value.latitude;
        $scope.center.lng = value.longitude;

        leafletData.getMap().then(function (map) {

          var marker = L.marker(new L.LatLng(value.latitude, value.longitude), {
            icon: L.icon({
              iconUrl: details.ripeness ? 'static/img/treemarker.png' : 'static/img/treemarker-red.png',
              iconSize: [32, 37], // size of the icon
              iconAnchor: [16, 16], // point of the icon which will correspond to marker's location
            }),
            title: value.name
          });
          map.addLayer(marker);

        });

        $scope.details = value;

        $scope.details.lastValue = data.items[1].value;

      });

      $http({
        url: '/trees/'+$routeParams.id+'/log'
      }).success(function (data) {

        var sData = [];
        var thresholdVal = 0;

        angular.forEach(data.items, function(value, key){
          if(!value.date_time) {
            thresholdVal = value.threshold;
            return true;
          }
          sData.push([
              new Date(value.date_time).getTime(),
              value.value
          ]);
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
              data: sData
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
                value: thresholdVal,
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
      });





    }])
;