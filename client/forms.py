from django import forms


class ClientRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=15,
                                 label="First Name:",
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control'
                                     }))
    last_name = forms.CharField(max_length=15,
                                label="Last Name:",
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }))
    user_name = forms.CharField(max_length=25,
                                label="Username:",
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }))
    email_id = forms.EmailField(label="Email",
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }))
    password1 = forms.CharField(max_length=16,
                                label="Password:",
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))
    password2 = forms.CharField(max_length=16,
                                label="Confirm Password:",
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))
    def clean_password2(self):
        data1 = self.cleaned_data['password1']
        data2 = self.cleaned_data['password2']

        if data1!=data2:
            raise forms.ValidationError("Password must be same!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data1