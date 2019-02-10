from . import views
from django.urls import path

urlpatterns = [
    path('hpux/', views.hpux, name='prt-hpux'),
    path('hpux/register', views.hpux_register, name='register'),
    path('hpux/hpux_register_data', views.hpux_register_data, name='hpux_register_data'),
    path('', views.home, name='prt-home'),
]
