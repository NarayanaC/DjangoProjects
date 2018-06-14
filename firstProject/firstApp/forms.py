from django import forms
from .models import Student_tab, auth_ext, csv_files
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student_tab
        fields = ['s_name', 's_class', 's_address', 's_phone']


class authentication_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    



class File_uploading(forms.ModelForm):
    class Meta:
        model = csv_files
        fields = ['file']

# class Extend(forms.ModelForm):
#     class Meta:
#         model = auth_user_extended
#         fields = ['is_role', 'is_designation', 'mobile_no', 'profile_image','user']



class ExtendedNew(forms.ModelForm):
    class Meta:
        model = auth_ext
        fields = ['designation','user']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # is_des = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# class Extend(forms.ModelForm):
#     is_role = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     is_designition = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     is_des = forms.CharField(max_length=30, required=False, help_text='Optional.')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','is_des' )