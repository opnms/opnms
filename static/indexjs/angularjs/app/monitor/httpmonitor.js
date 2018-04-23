angular.module('app', ['ui.bootstrap']).service('DataService', ['$rootScope',
    function($rootScope) {
    this.data = {};
    this.data.message = 'This is a message from a service';
    this.data.items = ['item1', 'item2', 'item3'];
    }
    ]).
controller('myModal', ['$scope', '$modalInstance', 'DataService',
    function($scope, $modalInstance, dataService) {
    $scope.data = dataService.data;
    $scope.message = dataService.data.message;
    $scope.items = dataService.data.items;
    $scope.selected = {
        item: $scope.items[0]
    };
    $scope.test = function(item){
        $scope.selected.item = item;
        }
        $scope.Submit = function() {
        $modalInstance.close($scope.selected.item);
        };
    $scope.cancel = function() {
        $modalInstance.dismiss('cancel');
        };
    }
    ]).
controller('appController', ['$scope','$modal','$log',function($scope, $modal, $log) {

//                    $scope.data = dataService.data;
    $scope.showModal = function() {
        var modalInstances = $modal.open({
            templateUrl: 'myModalContent.html',
            controller: 'myModal'
        });
        modalInstances.result.then(function(selectedItem) {
            $scope.selected = selectedItem;
            },function(){
            $log.info('Modal dismissed at :'+new Date())
        })
    };
    }]);