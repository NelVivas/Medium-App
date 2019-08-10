from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import PersonalUser

from users.forms import PersonalUserCreationForm, PersonalUserChangeForm

# Register your models here.
class PersonalUserAdmin(UserAdmin):
    
    add_form = PersonalUserCreationForm
    form     = PersonalUserChangeForm
    list_display = ['username', 'email', 'profile_photo']
    fieldsets = [
        (
            None, { 'fields' : ['username', 'email',] }
        ),
        (
            'User Information', { 'fields' : ['profile_photo', 'personal_info'] }    
        ),
    ]

    add_fieldsets = [
        (
            None, { 'fields' : ['username', 'email', 
                                'password1', 'password2'] }
        ),
        (
            'User Information', { 'fields' : ['profile_photo', 'personal_info'] }    
        ),
    ]




admin.site.register(PersonalUser,PersonalUserAdmin )
