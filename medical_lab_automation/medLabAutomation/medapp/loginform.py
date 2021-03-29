from django import forms  
from .models import User
  
class loginform(forms.ModelForm):  
    class Meta:
        password=forms.CharField(widget=forms.PasswordInput())  
        model = User 
        fields = ("email", "password")  