from django.urls import path
from calcapp import views

# app_name = 'calcapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.calc_result),
    path('join/', views.join, name='join'),
    path('ongoing/', views.ongoing, name='ongoing'),
    path('complete/', views.complete, name='complete'),
    path('group/', views.createGroup, name='creategroup'),
    path('payment/<int:group_id>', views.createPayment, name='createpayment'),
]