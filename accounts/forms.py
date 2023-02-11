from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django import forms
 
class SignUpForm(UserCreationForm):
    age = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('username', 'age', 'password1', 'password2')
        labels = { 'age': 'age'}

def save(self, commit=True):
	user = super(SignUpForm, self).save(commit=False)
	user.email = self.cleaned_data['email']
	if commit:
		user.save()
	return user