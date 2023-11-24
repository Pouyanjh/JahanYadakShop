from django.urls import path
from.views import GetListProduct, Topsellsviews, Getdetailproduct, Getproduct, Headlightview, Separview, Lentview, Radiatorview, mainproduct, getdetailshipping
from product import views

urlpatterns = [
    path('product/', GetListProduct.as_view()),
    path('topsells/', Topsellsviews.as_view()),
    path('product/id/<str:productid>/', Getdetailproduct.as_view()),
    path('product/brand/<str:brand>/', Getproduct.as_view()),
    path('separ/', Separview.as_view()),
    path('lent/', Lentview.as_view()),
    path('headlight/', Headlightview.as_view()),
    path('radiator/', Radiatorview.as_view()),
    path('<str:pk>/pay/', views.payorder, name='pay-order'),
    path('api/result/', views.Idpaycallback, name='idpaycallback'),
    path('<str:pk>/inquirypay', views.inquirypay, name='inquirypay'),
    path('mainproduct/', mainproduct.as_view()),
    path('add/order/', views.addorderview, name='order-add'),
    path('shipping/', views.shippingadd, name='shipping'),
    path('shipping/id/<str:id>/', views.getdetailshipping.as_view()),
]
