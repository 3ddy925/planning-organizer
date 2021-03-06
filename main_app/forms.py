from django import forms
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ('name', 'date', 'time', 'description',)

class SignupForm(UserCreationForm):
  first_name = forms.CharField(max_length=20, required=True)
  last_name = forms.CharField(max_length=30, required=True)
  email = forms.EmailField(max_length=200, help_text='Required')

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class EditProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username',)