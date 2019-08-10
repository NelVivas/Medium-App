from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import PersonalUser

class PersonalUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PersonalUser
        fields = UserCreationForm.Meta.fields + ('profile_photo', 'personal_info')

class PersonalUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = PersonalUser
        fields = ['username',  
                  'profile_photo', 'personal_info']
