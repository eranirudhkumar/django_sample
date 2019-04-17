import string
import random
from django.shortcuts import render, redirect
from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm,
                                       UserChangeForm)
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import urllib.request
import urllib.parse

from . import forms as users_forms


def sendSMS(apikey, numbers, sender, message):
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
                                   'message': message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return (fr)


# Create your views here.
def home(request):
    return render(request,
                  'users/home.html',
                  {"name": "Anirudh"})


def users_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("Username:", username, '\n'
                                         'Password:', password)
            user = authenticate(request,
                                username=username,
                                password=password)
            login(request, user)
            return redirect('users_home')
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def users_registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            otp = "".join([random.choice(string.digits) for i in range(4)])
            resp = sendSMS('P1mM6VgA66U-fhcM3etpeRWFDikqzACm3Y1naVudeB',
                           '919541214954',
                           'Jims Autos',
                           'Your OTP is ' +
                           str(otp) +
                           "please don't share with any one.")
            print("Otp sent:", resp)

            # form.save()
            request.session['otp_form'] = form
            request.session['otp'] = otp
            return redirect('users_otp')
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required(login_url='users_login')
def users_change(request):
    # form = UserChangeForm(instance=request.user)
    form = users_forms.UserUpdateForm(instance=request.user)
    if request.method == 'POST':
        # form = UserChangeForm(request.POST,
        #                       instance=request.user)
        form = users_forms.UserUpdateForm(request.POST,
                                          instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('users_home')

    context = {
        'form': form
    }
    return render(request, 'users/users_change.html',
                  context)


def users_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users/users_users.html', context)


def otp_validation(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if 'otp' in request.session:
            otp_val = request.session['otp']
            if otp == otp_val:
                form = request.session['otp_form']
                form.save()
                return redirect('users_login')
            return redirect('users_regiter')
    return render(request, 'users/otp_validation.html')
