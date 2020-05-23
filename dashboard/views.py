from django.http import HttpResponse
from django.shortcuts import render

things = [
    {
        'name': 'Coffee Machine',
        'lifetime_used': 152,
        'mfg_date': '04/12/2018',
        'last_cleaned': '04/05/2020',
        'max_lifetime': 1555
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
    context = {
        'things': things,
        'title': 'My Devices'
    }
    return render(request, 'dashboard/home.html', context)


def not_found(request):
    return HttpResponse("<h1>No Such Path! Lost ?</h1>")
