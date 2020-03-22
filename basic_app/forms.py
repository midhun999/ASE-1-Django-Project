from django import forms
from django.contrib.auth.models import User
from basic_app.models import ShopKeeperRegistration,UserFeedback

from phone_field import PhoneField

class ShopKeeperRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())
    #phone_number = PhoneField(blank=True,help_text='Contact phone number with country code')

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password',)

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = ShopKeeperRegistration
        fields = ('phone_number',)


class UserFeedbackForm(forms.ModelForm):

    class Meta():
        model = UserFeedback
        fields = '__all__'