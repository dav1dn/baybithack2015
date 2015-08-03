# pylint: disable=line-too-long
from django import forms
from django.forms.widgets import PasswordInput


class RegisterForm(forms.Form):

    TSHIRT_SIZE_CHOICES = (
        ('extra small', "Adult Extra Small"),
        ('small', "Adult Small"),
        ('medium', "Adult Medium"),
        ('large', "Adult Large"),
        ('extra large', "Adult Extra Large"),
    )

    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email", max_length=254)
    school = forms.CharField(label="School", max_length=256)
    tshirt_size = forms.ChoiceField(label="T-shirt size", choices=TSHIRT_SIZE_CHOICES)
    vegetarian = forms.BooleanField(label="Check if you are a vegetarian", required=False)
    source = forms.CharField(label="Where did you hear about this event?", max_length=256)
    password = forms.CharField(label="Password for your Bay Bithack account", max_length=256,
            widget=PasswordInput())
