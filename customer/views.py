from django.shortcuts import render
from . import models as customer_models


# Create your views here.
def customer_home(request):
    states = customer_models.State.objects.all()
    distrcts = customer_models.District.objects.all()
    context = {
        'states': states,
        'districts':distrcts
    }
    return render(request, 'customer/home.html',
                  context)

def customer_state(request):
    if request.method=='GET':
        state_name=request.GET['state_name']
        print(state_name)

    states = customer_models.State.objects.filter(state_name=state_name)
    # distrcts = customer_models.District.objects.all()
    distrcts = customer_models.District.objects.filter(state=states.first().id)
    context = {
        'districts':distrcts
    }
    return render(request,
                  'customer/customer_state.html',
                  context)