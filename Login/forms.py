from django import forms
from .models import UserData

class RegistrationForm(forms.ModelForm):
    class Meta:
        model =UserData
        fields =['f_name', 'l_name', 'username', 'password', 'cn_password', 'city' ,'phone_number' ,'prn_number' ,'gender','clg_name']
