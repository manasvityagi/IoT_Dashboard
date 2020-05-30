from django.urls import path


from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='dashboard-home'),
    # path('', views.not_found, name='404')
]

