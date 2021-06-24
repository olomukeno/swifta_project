from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Password")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('Sorry, this email address is already in use.')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar"]






