from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

FIELDS_PLACEHOLDERS = {
    'email': "Email address",
    'first_name': "First name",
    'last_name': "Last name",
    'username': "Username",
    'password': "&#9679;&#9679;&#9679;&#9679;&#9679;",
}

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = FIELDS_PLACEHOLDERS[field]
            self.fields[field].label = ''

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = FIELDS_PLACEHOLDERS[field]
            self.fields[field].label = ''

