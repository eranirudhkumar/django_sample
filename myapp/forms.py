from django.forms import ModelForm
from .models import Student
from django import forms


class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    # class FoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # super(StudentModelForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class StudentLoginModelForm(forms.Form):
    # class Meta:
    #     model = Student
    #     fields = ['email', 'password']

    # class FoodForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     # super(StudentModelForm, self).__init__(*args, **kwargs)
    #     super().__init__(*args, **kwargs)
    #     for field in iter(self.fields):
    #         self.fields[field].widget.attrs.update({
    #             'class': 'form-control'
    #         })
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

    def clean_password(self):
        data = self.cleaned_data.get('password', '')
        if len(data) >= 6 and len(data) <= 16:
            return data
        raise forms.ValidationError("Please enter valid password.!!!")
