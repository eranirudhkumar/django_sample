from django.shortcuts import render
from django.shortcuts import redirect
from . import forms as client_forms
from django.contrib.auth import models as auth_models
from django.contrib.auth.hashers import make_password


# Create your views here.

def client_home(request):
    return render(request, 'client/client_home.html')


def client_registration(request):
    form = client_forms.ClientRegisterForm()
    if request.method == 'POST':
        form = client_forms.ClientRegisterForm(data=request.POST)
        if form.is_valid():
            # print("Form:",dir(form))
            # print("Form:",form.cleaned_data)
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('user_name')
            email = form.cleaned_data.get('email_id')
            password = make_password(form.cleaned_data.get('password1'))

            user = auth_models.User()
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.password = password
            user.save()
            return redirect('client_home')

    context = {
        'form': form
    }
    return render(request,
                  'client/client_register.html',
                  context)
