from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=20,
                               widget = forms.PasswordInput)
    password_confirm = forms.CharField(max_length=20,
                               widget = forms.PasswordInput,
                                label = "Confirm password")

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password_confirm"
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        #check if the passwords match

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match!!!")

        return cleaned_data