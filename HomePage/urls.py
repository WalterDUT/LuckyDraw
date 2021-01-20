from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
# from django.contrib.auth import views as login
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='pages/home.html'), name='logout'),
    path('simpleupload/',views.simple_upload, name='simple_upload'),
    path('form/', views.model_form_upload, name='model_form_upload'),
]
