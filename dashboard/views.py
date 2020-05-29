from decouple import config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from users.async_tasks import send_email
from .forms import add_device, add_manufacturer
from .models import Thing, Manufacturer, Address

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


@login_required
def home_view(request):
    context = {
        'things': things,
        'title': 'My Devices'
    }

    return render(request, 'dashboard/deviceCard.html', context)


def add_device(request):
    if request.method == 'POST':

        form = add_device(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('Congrats, Your new device is ready!')

    # if a GET (or other method) create a blank form
    else:
        form = add_device()

    return render(request, 'dashboard/addDevice.html', {'form': form})


def about(request):
    return render(request, 'dashboard/about.html')


def not_found(request):
    return HttpResponse("<h1>No Such Path! Lost ?</h1>")


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
            return HttpResponse('Invalid Form, Probably the manufacturer already exists')


class AddAddressView(CreateView):
    def get(self, request):
        existing_addresses = Address.objects.all()
        form = add_manufacturer(request.POST)
        context = {
            'form': form,
            'existing_manufacturers': existing_addresses
        }
        return render(request, 'dashboard/addManufacturer.html', context)

    def post(self, request):
        form = add_manufacturer(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('New Manufacturer Added!')
