from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import RegistrationForm
from .forms import LoginForm


# Create your views here.
def index(request):
    # response = HttpResponse()
    # response.writelines('<h1>Xin chào</h1>')
    # response.write('Đây là app home')
    # return response
    return render(request, 'pages/home.html')


# Create your views here.
def contact(request):
    return render(request, 'pages/contact.html')


def error404(request, exception):
    return render(request, exception, 'pages/error.html')


def error500(request):
    return render(request, 'pages/error.html')


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    return render(request, 'pages/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(username=cd['username'],
                                     password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid account')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})


# def auth_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect('/pages/home.html')
#     else:
#         return HttpResponseRedirect('/pages/login.html')


def logout():
    return None
