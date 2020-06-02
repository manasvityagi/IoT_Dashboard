from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views as dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user_views.registration, name="signup"),
    # class based views with login required
    path('profile/', login_required(user_views.OwnerView.as_view()), name="profile"),
    path('about/', dashboard_view.about, name="about"),
    path('add_device/', login_required(dashboard_view.AddDeviceView.as_view()), name="add_device"),
    path('add_address/', login_required(dashboard_view.AddAddressView.as_view()), name="add_address"),
    path('add_manufacturer/', login_required(dashboard_view.AddManufacturerView.as_view()), name="add_manufacturer"),
    path('add_device_model/', login_required(dashboard_view.AddDeviceModelsView.as_view()), name="add_device_model"),
    path('add_home/', login_required(dashboard_view.AddHomeView.as_view()), name="add_home"),
    path('add_service_provider/',
         login_required(dashboard_view.AddServiceProviderView.as_view()), name="add_service_provider"),
    path('add_seller/', login_required(dashboard_view.AddSellerView.as_view()), name="add_seller"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('', include('dashboard.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # TODO set it up, correctly for production
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
