from django import forms
from login.models import Login

class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Login
        fields = ('username', 'password',)