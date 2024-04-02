from django import forms
from .models import Students
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'adm_no', 'profile_picture']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'adm_no': 'Admission Number',
            'profile_picture': 'Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'adm_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
