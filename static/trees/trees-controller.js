'use strict';

/* Controllers */

angular.module('droopal')
    .controller('TreesCtrl', ['$scope', 'leafletData', '$http', function ($scope, leafletData, $http) {

      var addressPoints = [
        [-37.8210922667, 175.2209316333, "2"],
        [-37.8210819833, 175.2213903167, "3"],
        [-37.8210881833, 175.2215004833, "3A"],
        [-37.8211946833, 175.2213655333, "1"],
        [-37.8209458667, 175.2214051333, "5"],
        [-37.8208292333, 175.2214374833, "7"],
        [-37.8325816, 175.2238798667, "537"],
      ];

      $http({
        url: '/trees'
      }).success(function (data) {
        leafletData.getMap().then(function (map) {


          var markers = new L.MarkerClusterGroup();

          angular.forEach(data.items, function(value, key){
            var marker = L.marker(new L.LatLng(value.latitude, value.longitude), {
              icon: L.icon({
                iconUrl: 'static/img/treemarker-red.png',//'img/treemarker.png',
                iconSize: [32, 37], // size of the icon
                iconAnchor: [16, 16], // point of the icon which will correspond to marker's location
              }),
              title: value.name
            });
            marker.bindPopup(value.name);
            markers.addLayer(marker);
          });

          map.addLayer(markers);
        });

        $scope.trees = data.items;

        angular.forEach(data.items, function(value, key) {
          value.ripeStatus = value.ripeness ? 'Ripe' : 'Not Ripe';
        });

      });


      angular.extend($scope, {
        defaults: {
          scrollWheelZoom: false
        },
        center: {
          lat: 33.7550,
          lng: -84.3900,
          zoom: 11
        }
      });


    }]);