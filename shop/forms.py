from django import forms

from shop.models import OrderItem, Product


class CustomerForm(forms.Form):
    name = forms.CharField(max_length=80)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=150)
    price = forms.CharField(max_length=300, label="Price ($)")

class UpdatePriceForm(forms.Form):
    your_product = forms.ModelChoiceField(queryset=OrderItem.objects.all(), label="Select Product")
    # your_product_id_and_name = forms.ModelChoiceField(queryset=OrderItem.objects.values_list('product__id', 'product__name').distinct(), label="Your Product ID and Name (ID, Name)")
    your_product_ID = forms.IntegerField()
    new_price = forms.DecimalField(label="New Price ($)")


class AddToBasketForm(forms.Form):
    product_id = forms.ModelChoiceField(queryset=Product.objects.all(), label="Select Product")
    quantity = forms.IntegerField(min_value=1, initial=1)