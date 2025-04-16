from django.contrib.auth import get_user_model
User = get_user_model()

# authentication/forms.py
from django import forms

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','password']




class UserCreationForm(forms.ModelForm):
    CHOICES = (
        ('Admin','Admin'),('Gérant','Gérant'),('Caissier','Caissier')
    )
    user_type=forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
    )
    class Meta:
        model = User
        fields = ['username','email','password','user_type']