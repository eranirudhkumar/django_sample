from django.shortcuts import render


# Create your views here.

def account_home(request):
    return render(request, 'account/home.html')
