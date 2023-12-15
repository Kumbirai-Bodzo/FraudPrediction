from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

        self.fields['username'].widget.attrs.update({'class': 'form-control'})

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})