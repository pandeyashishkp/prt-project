from django.shortcuts import render
from .forms import HpuxForm
from .models import Hpux
import re


def home(request):
    return render(request, 'hpux/home.html')


def hpux(request):
    return render(request, 'hpux/hpux.html')


def hpux_register(request):
    return render(request, "hpux/register.html")


def hpux_register_data(request):
    servername = request.POST['servername']
    change_number = request.POST['change_number']
    email = request.POST['email']
    date = request.POST['date']
    patch_bundle = request.POST['patch_bundle']
    if not re.search(r'^CRQ[0-9]{10}$', change_number):
        return render(request, "hpux/error.html", {'error': 'change_number is not in specified format- CRQ0000XXXXXX'})
    elif not re.search(r'vodafone\.com$', email):
        return render(request, "hpux/error.html", {'error': 'Please specify company email address'})
    else:
        update = Hpux(servername=servername, change_number=change_number,
                      email=email, date=date, patch_bundle=patch_bundle)
        update.save()
        return render(request, "hpux/register.html")
