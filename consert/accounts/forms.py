from django import forms
from .models import ProfileModel
from django.contrib.auth.forms import UserChangeForm

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = ProfileModel
        fields = ['gender','profileimage','credit']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['gender','profileimage','credit']

class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name','last_name','email']
    password = None
