from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def info(request):
    return HttpResponse("<h1>Dashboard Home Info</h1>")


def not_found(request):
    return HttpResponse("<h1>No Such Path! Lost ?</h1>")
