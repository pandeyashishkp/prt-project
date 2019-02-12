from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='prt-home'),
    path('hpux/', views.hpux, name='prt-hpux'),
    path('hpux/register', views.hpux_register, name='register'),
    path('hpux/hpux_register_data', views.hpux_register_data, name='hpux_register_data'),
    path('hpux/delete', views.delete, name='delete'),
    path('hpux/hpux_delete_data', views.hpux_delete_data, name='hpux_delete_data'),
]
