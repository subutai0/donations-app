from django.urls import path
from . import views

urlpatterns = [
    path('', views.charity_list, name='charity_list'),
    path('<int:charity_id>/donate/', views.Charity, name='donate'),
    path('payment/execute/', views.payment_execute, name='payment_execute'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
]
