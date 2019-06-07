from django import forms
from django.contrib.auth.models import User
from users_pass_app.models import UserProfileData

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email' , 'password')
class UserProfileDataForm(forms. ModelForm):
    class Meta():
        model = UserProfileData
        fields = ('portfolio_data', 'profile_image')
