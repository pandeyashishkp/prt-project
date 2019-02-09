from django.shortcuts import render
from .forms import HpuxForm


def home(request):
    return render(request, 'hpux/home.html')


def hpux(request):
    return render(request, 'hpux/hpux.html')


def hpux_create_view(request):
    form = HpuxForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, "hpux/hpux_create.html", context)
