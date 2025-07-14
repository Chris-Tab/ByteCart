from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        label='Full Name',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
                }
                )
        )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
                }
                )
        )
    content = forms.CharField(
        label='Message',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your message here'
                }
                )
        )
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@example.com"):
            raise forms.ValidationError("Email must be from the example.com domain.")
        return email
    

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
                }
                )
        )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
                }
                )
        )
    
class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username'
                }
                )
        )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
                }
                )
        )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Choose a password'
                }
                )
        )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password'
                }
                )
        )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email   


    def clean(self):
        data= self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Passwords do not match.")
        return data