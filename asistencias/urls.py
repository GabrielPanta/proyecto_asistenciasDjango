from django.urls import path
from . import views

urlpatterns = [
    path('', views.consulta, name='consulta'),
    path('admin/', views.login_admin, name='login_admin'),
    path('panel/', views.admin_panel, name='admin_panel'),
    path('logout/', views.logout_admin, name='logout_admin'),
]
