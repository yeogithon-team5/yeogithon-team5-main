from django.urls import path
from calcapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group/', views.create, name='creategroup'),
    path('payment/<int:group_id>', views.create, name='createpayment'),
]