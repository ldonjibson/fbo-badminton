from django import forms


class KeyForm(forms.Form):
    key = forms.CharField(label='Enter unique key', max_length=32)
