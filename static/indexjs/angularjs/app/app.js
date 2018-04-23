var app = angular.module('monitor',['ui.bootstrap']);
app.controller('ModalDemoCtrl',function ($scope,$uibModal,$log) {
    $scope.showForm = function () {
        $scope.message = "Show Form Button Clicled";
        console.log($scope.message);

        var modalInstance = $uibModal.open({
             templateUrl: 'myModalContent.html',
                controller: ModalDemoCtrl,
                backdrop: "static",
                resolve: {
                    userForm: function () {
                        return $scope.userForm;
                    }
                }
        });
        modalInstance.result.then(function (selectedItem) {
            $scope.selected = selectedItem;
        },function () {
            $log.info('Modal dismissed at:' + new Date());
        });

    };
});

var ModalDemoCtrl = function ($scope, $uibModalInstance, userForm) {
    $scope.form = {}
    $scope.submitForm = function () {
        if ($scope.form.userForm.$valid) {
            console.log('user form is in scope');
            $uibModalInstance.close('$scope.selected.item');
        } else {
            console.log('userform is not in scope');
        }
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };
};
