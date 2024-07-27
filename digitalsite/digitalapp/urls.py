from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('product/<int:id>', views.detail, name='detail'),
    path('success/', views.payment_success_view, name='success'),
    path('failed/', views.payment_failed_view, name='failed'),
    path('api/checkout-session/<int:id>/', views.create_checkout_session, name='api_checkout_session'),
    
]