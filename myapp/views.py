from django.shortcuts import (render,
                              redirect)
from .models import Student
from .forms import (StudentModelForm,
                    StudentLoginModelForm)
from django.contrib import  messages
from django.views.generic import TemplateView
from rest_framework.views import APIView,Response
from .serializers import StudentSerializer


# from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='app_login-student')
def home(request):
    if 'logout' in request.GET:
        # print(request.GET)
        del request.session['st_user']
        request.session.modified = True

        messages.add_message(request, messages.SUCCESS, 'Logout successfully.')

    if 'st_user' not in request.session:
        return redirect('app_login-student')

    student = request.session.get('st_user')
    context = {
        'all_student': Student.objects.all(),
        'name': student
    }
    return render(request, 'myapp/home.html', context)


def add_student(request):
    form = StudentModelForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(name,email)
        st = Student(name=name,
                     email=email,
                     password=password)
        st.save()
        return redirect('app_home')
    context = {
        'form': form
    }
    return render(request, 'myapp/student/add_student.html',
                  context)


def login_student(request):
    if 'st_user' in request.session:
        return redirect('app_home')
    form = StudentLoginModelForm()
    if request.method == 'POST':
        form = StudentLoginModelForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            # print("Email:", email)
            # print("Password:", password)
            student = Student.objects.filter(email=email,
                                             password=password)
            # print("Student:", student)
            if student.exists():
                request.session['st_user'] = student.first().name
                return redirect('app_home')
            else:
                form.clean()
    context = {
        'form': form
    }
    return render(request, 'myapp/student/login_student.html',
                  context)


class HomeView(TemplateView):
    # template_name='myapp/home.html'
    pass

class StudentApiView(APIView):
    # template_name='myapp/api/student_api_view.html'

    def get(self, request):
        student = Student.objects.all()
        serialize = StudentSerializer(student, many=True)
        return Response(serialize.data)

# git added