from django.contrib.auth.forms import UserCreationForm, forms
from django.forms import ModelForm, Field
from . import models
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # q = forms.CharField(label='search', 
    #                 widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password1', 'password2']


