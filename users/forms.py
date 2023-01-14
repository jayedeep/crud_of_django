# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Student
from django.db.models import Q

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email', 'mobile_number', 'birth_date')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'mobile_number', 'birth_date')


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


    def clean_username(self):

        username = self.cleaned_data['username']
        if not CustomUser.objects.filter(Q(username=username)|Q(email=username)).exists():
            raise forms.ValidationError('User exiest with this username')
        return username

class RegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    mobile_number=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        print(">>>>>username",username)

        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('User with this username already exiest')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        print(">>>>>email",email)
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exiest')
        return email

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        password=self.cleaned_data['password']
        confirm_password=self.cleaned_data['confirm_password']
        if password!=confirm_password:
            raise forms.ValidationError('Password and Confirm password are not matched')
        return cleaned_data


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'roll_no':forms.NumberInput(attrs={'class':'form-control'}),
            
        }