from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('date_of_birth','photo')



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
class UserRegistration(forms.Form):
     password = forms.CharField(label="password",widget=forms.PasswordInput)
     password2 = forms.CharField(label="Repeat Password",widget=forms.PasswordInput)
     
     class Meta:
         model =User
         fields =('username','first_name','email')
         
     def clean_password2(self):
         cd =self.cleaned_data
         if cd['password'] !=cd['password2']:
             raise forms.ValidationError('Passwords don\'t match')
         return cd['password2']

         
     
#user creation form in django.contruib.auth.forms
class signUp(UserCreationForm):
    email = forms.EmailField(max_length=100,help_text='required.Enter a valid email address')
    
    class meta:
        model = User
        fields = ('user','email','password1','password2')