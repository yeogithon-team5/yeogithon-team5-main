from django.urls import path
from calcapp import views

app_name = 'calcapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.calc_result),
    path('group/', views.create, name='creategroup'),
    path('payment/<int:group_id>', views.create, name='createpayment'),
]