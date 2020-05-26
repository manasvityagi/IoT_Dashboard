from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='dashboard-home'),
    # path('', views.not_found, name='404')
]