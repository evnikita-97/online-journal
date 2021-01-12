from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name=forms.CharField(max_length=40)
    email_id=forms.CharField(max_length=40)
    password= forms.CharField(max_length=50)
    location=forms.CharField(max_length=30)

    class Meta:
        model=User
        fields=('name','email_id','password','location')
       
class Journal_User(UserCreationForm):
    user=forms.CharField(max_length=40)
    summary=forms.TimeField()

    