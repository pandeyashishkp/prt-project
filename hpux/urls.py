from . import views
from django.urls import path

urlpatterns = [
    path('hpux/', views.hpux, name='prt-hpux'),
    path('', views.home, name='prt-home'),
]
