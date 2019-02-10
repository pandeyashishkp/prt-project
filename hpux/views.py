from django.shortcuts import render
from .forms import HpuxForm
from .models import Hpux


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
    update = Hpux(servername=servername, change_number=change_number,
                  email=email, date=date, patch_bundle=patch_bundle)
    update.save()
    return render(request, "hpux/register.html")
