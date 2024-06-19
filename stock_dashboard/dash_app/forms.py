from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from . models import studentrecord

from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput, TextInput

from django.db import models

from django import forms

# Register/Create User

class RegisterUser(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']

# Login User

class LoginUser(AuthenticationForm):
     username = forms.CharField(widget=TextInput())
     password = forms.CharField(widget=PasswordInput())
     
# Create Record 

# class StockForm(forms.ModelForm):
#     class Meta:
#         model = stock
#         fields = ['shortname', 'stockname', 'option', 'quantity', 'price']
class StockForm(forms.Form):
    shortname = forms.CharField(max_length=5)
    stockname = forms.CharField(max_length=200)
    class Option(models.TextChoices):
        BUY = 'BUY', 'Buy'
        SELL = 'SELL', 'Sell'
    option = forms.ChoiceField(choices=Option.choices, initial=Option.BUY)
    quantity = forms.IntegerField()
    price = forms.DecimalField(max_digits=7, decimal_places=2)

