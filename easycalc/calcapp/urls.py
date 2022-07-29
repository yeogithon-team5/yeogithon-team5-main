from django.urls import path
from . import views


app_name = 'calcapp'

urlpatterns = [
    path('<int:pk>/', views.calc_result),
]
