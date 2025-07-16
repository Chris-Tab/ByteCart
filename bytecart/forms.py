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
    

