 var routeModule = angular.module('routeModule',['ngRoute']);
routeModule.controller(['$routeProvider',
function ($routeProvider) {
    $routeProvider.
    when('/addOrder',{
        templateUrl:'templates/server/add-order.html',
        controller:'AddOrderController'
    }).
    when('/showOrders',{
        templates:'/server/show-orders.html',
        controller:'ShowOrdersController'
    }).
        otherwise({
        redirectTo:'/addOrder'
    });
}]);