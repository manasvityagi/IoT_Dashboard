from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='dashboard-info'),
    # path('', views.not_found, name='404')
]