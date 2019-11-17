from django import forms
from .models import Store


class AddMenuForm(forms.Form):
    menu_name = forms.CharField(label='Menu name', max_length=100)
    store_name = forms.ModelChoiceField(queryset=Store.objects.all())
    price = forms.IntegerField(label='Price')


class AddStoreForm(forms.Form):
    store_name = forms.CharField(label='Store name', max_length=100)
    location = forms.CharField(max_length=200)
    tel = forms.CharField(max_length=20)
