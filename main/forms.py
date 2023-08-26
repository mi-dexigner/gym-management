from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields =('full_name','email','phone','message')

class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username','password1', 'password2')

