from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.

from .models import Profile, Transaction, Stock
from .forms import CreateUserForm, CreateProfileForm
# import yfinance as yf
# import pandas as pd

# msft = yf.Ticker("MSFT")
# get stock info
# msft.info
# get historical market data
# hist = msft.history(period="max")

def registerPage(request):
    user_form = CreateUserForm
    profile_form = CreateProfileForm

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        profile_form = CreateProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('login')

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, "accounts/register.html", context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect('account.html')

    context = {}
    return render(request, "accounts/login.html", context)

def index(request):
    context = {}
    return render(request, "stocks/index.html", context)

def test(request):
    return HttpResponse('Routing test passed!', context)