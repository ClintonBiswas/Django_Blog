from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import userProfile

class singupFrom(UserCreationForm):
    #firstname = forms.CharField(label = "First Name", required = True)
    #lastname = forms.CharField(label = "Last Name", required = False)
    email = forms.EmailField(label ="Email Address",required = True)
    class Meta():
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

class userprofilechange(UserChangeForm):
    class Meta():
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')

class Profilepic(forms.ModelForm):
    class Meta():
        model = userProfile
        fields = ['profile_pic']
