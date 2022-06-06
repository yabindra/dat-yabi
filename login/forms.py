from django import forms
# Create your models here.
class Loginform(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget = forms.PasswordInput)