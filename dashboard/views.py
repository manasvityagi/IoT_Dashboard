from django.http import HttpResponse
from django.shortcuts import render, redirect

from IoT_Dashboard import settings
from .models import Things

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


# Create your views here.
def info(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGOUT_REDIRECT_URL, request.path))
    context = {
        'things': things,
        'title': 'My Devices'
    }
    t1 = Things(description="Coffee Machine in Kitchen", )
    return render(request, 'dashboard/deviceCard.html', context)


def add_thing(request):



def not_found(request):
    return HttpResponse("<h1>No Such Path! Lost ?</h1>")
