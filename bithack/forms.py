from django import forms


class RegisterForm(forms.Form):

    TSHIRT_SIZE_CHOICES = (
        ('extra small', "Adult Extra Small"),
        ('small', "Adult Small"),
        ('medium', "Adult Medium"),
        ('large', "Adult Large"),
        ('extra large', "Adult Extra Large"),
    )

    name = forms.CharField(label="Full Name", max_length=100)
    # TODO change this to email field
    email = forms.CharField(label="Email", max_length=256)
    school = forms.CharField(label="School", max_length=256)
    tshirt_size = forms.CharField(label="T-shirt size", max_length=30, choices=TSHIRT_SIZE_CHOICES)
    vegetarian = forms.BooleanField(label="Vegetarian options", default=False)
