from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone', 'address', 'password']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        user_profile = UserProfile(
            user=user,
            phone=self.cleaned_data['phone'],
            address=self.cleaned_data['address']
        )
        if commit:
            user_profile.save()
        return user_profile

