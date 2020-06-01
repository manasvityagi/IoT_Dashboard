from decouple import config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from users.tasks import send_email
from .forms import *
from .models import *

# Todo, should be better If I add the views in logical order, for better readability

things = [
    {
        'name': 'Coffee Machine',
        'lifetime_used': 152,
        'mfg_date': '04/12/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 4999
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5000
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5001
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5002
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5003
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5004
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5005
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5006
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5007
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5008
    },
    {
        'name': 'Vacuum Cleaner',
        'lifetime_used': 167,
        'mfg_date': '04/11/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 5009
    }
]


# function based view
@login_required
def home_view(request):
    logged_in_user = request.user
    x = Home.objects.filter(owner=logged_in_user)
    context = {
        'things': Thing.objects.filter(installed_home_id__owner=logged_in_user),
        'title': 'My Devices'
    }
    Thing.objects.all()
    return render(request, 'dashboard/deviceCard.html', context)


class AddDeviceView(CreateView):

    def get(self, request):
        existing_installed_devices = Thing.objects.all()
        form = add_device(request.POST)
        context = {
            'form': form,
            'existing_installed_devices': existing_installed_devices
        }
        return render(request, 'dashboard/addDevice.html', context)

    def post(self, request):
        form = add_device(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('New Device Installed!')



# def AddDeviceView(request):
#     if request.method == 'POST':
#         form = add_device(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Congrats, Your new device is ready!')
#
#     # if a GET (or other method) create a blank form
#     else:
#         form = add_device()

#    return render(request, 'dashboard/addDevice.html', {'form': form})


def about(request):
    return render(request, 'dashboard/about.html')


def not_found(request):
    return HttpResponse("<h1>No Such Path! Lost ?</h1>")


# class based views from here on
class AddAddressView(CreateView):
    def get(self, request):
        existing_addresses = Address.objects.all()
        form = add_address(request.POST)
        context = {
            'form': form,
            'existing_addresses': existing_addresses
        }
        return render(request, 'dashboard/addAddress.html', context)

    def post(self, request):
        form = add_address(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('New Address Added!')


class AddManufacturerView(CreateView):

    def get(self, request):
        existing_manufacturers = Manufacturer.objects.all()
        form = add_manufacturer(request.POST)
        context = {
            'form': form,
            'existing_manufacturers': existing_manufacturers
        }
        return render(request, 'dashboard/addManufacturer.html', context)

    def post(self, request):
        form = add_manufacturer(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form.non_field_errors()
            return HttpResponse('New Manufacturer Added!')
        else:
            form.non_field_errors()
            field_errors = [(field.label, field.errors) for field in form]
            errors = str(field_errors)
            return HttpResponse('Invalid Form, Reason -> ' + errors)


class AddDeviceModelsView(CreateView):

    def get(self, request):
        existing_device_models = DeviceModels.objects.all()
        form = add_device_models(request.POST or None)
        context = {
            'form': form,
            'existing_device_models': existing_device_models
        }
        return render(request, 'dashboard/addDeviceModel.html', context)

    def post(self, request):
        form = add_device_models(request.POST or None)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form.non_field_errors()
            return HttpResponse('New Device Model Added to Catalogue, now you can add them to your !')
        else:
            form.non_field_errors()
            field_errors = [(field.label, field.errors) for field in form]
            errors = str(field_errors)
            # TODO should display specific error in formatted manner
            return HttpResponse('Invalid Form, Reason -> ' + errors)


class AddHomeView(CreateView):
    def get(self, request):
        existing_homes = Home.objects.all()
        form = add_home(request.POST)
        context = {
            'form': form,
            'existing_homes': existing_homes
        }
        return render(request, 'dashboard/addHome.html', context)

    def post(self, request):
        form = add_home(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form.non_field_errors()
            return HttpResponse('New Home Added!')
        else:
            form.non_field_errors()
            field_errors = [(field.label, field.errors) for field in form]
            errors = str(field_errors)
            # TODO should display specific error in formatted manner
            return HttpResponse('Invalid Form, Reason -> ' + errors)


class AddServiceProviderView(CreateView):
    def get(self, request):
        existing_provider = ServiceProvider.objects.all()
        form = add_service_provider(request.POST)
        context = {
            'form': form,
            'existing_provider': existing_provider
        }
        return render(request, 'dashboard/addServiceProvider.html', context)

    def post(self, request):
        form = add_service_provider(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form.non_field_errors()
            return HttpResponse('New Service Provider Added!')
        else:
            form.non_field_errors()
            field_errors = [(field.label, field.errors) for field in form]
            errors = str(field_errors)
            # TODO should display specific error in formatted manner
            return HttpResponse('Invalid Form, Reason -> ' + errors)


class AddSellerView(CreateView):
    def get(self, request):
        existing_seller = ServiceProvider.objects.all()
        form = add_seller(request.POST)
        context = {
            'form': form,
            'existing_seller': existing_seller
        }
        return render(request, 'dashboard/addSeller.html', context)

    def post(self, request):
        form = add_seller(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form.non_field_errors()
            return HttpResponse('New Seller Added!')
        else:
            form.non_field_errors()
            field_errors = [(field.label, field.errors) for field in form]
            errors = str(field_errors)
            # TODO should display specific error in formatted manner
            return HttpResponse('Invalid Form, Reason -> ' + errors)
