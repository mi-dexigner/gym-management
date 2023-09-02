from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
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

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','first_name', 'last_name', 'email')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude the password field from the form
        self.fields.pop('password')

        # Make the 'username' field readonly
        self.fields['username'].widget.attrs['readonly'] = True

