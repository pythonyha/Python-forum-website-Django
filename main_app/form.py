from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, help_text='نام کاربری شما')
    email = forms.EmailField(max_length=254, help_text='ایمیل شما')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
