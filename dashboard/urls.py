from django.urls import path
from . import views

urlpatterns = [
    path('/info/', views.info, name='dashboard-info'),
    path('', views.not_found, name='404')
]