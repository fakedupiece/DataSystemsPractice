from django import forms


class CustomerForm(forms.Form):
    name = forms.CharField(max_length=80)
    address = forms.CharField(max_length=500)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=150)
    price = forms.CharField(max_length=300)