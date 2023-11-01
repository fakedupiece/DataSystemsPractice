from django.shortcuts import render
from .forms import CustomerForm, ProductForm
from .models import Customer, Address, Product, OrderItem

def index_shop(request):
    pass

def create_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            name = customer_form.cleaned_data['name']
            address = customer_form.cleaned_data['address']
            b = Customer(name=name)
            c = Address(address=address)
            b.save()
            c.save()
            return render(request, "model_saved.html", {'messages': ['New Customer' + ' saved!']})
    # if a GET (or any other method) we'll create a blank form
    else:
        customer_form = CustomerForm()

        return render(request, 'main.html', {'customer_form': customer_form})

def create_product(request):
    if request.method == 'POST':
        product_form = CustomerForm(request.POST)
        if product_form.is_valid():
            name = product_form.cleaned_data['name']
            price = product_form.cleaned_data['address']
            b = Product(name=name)
            c = OrderItem(price=price)
            b.save()
            c.save()
            return render(request, "model_saved.html", {'messages': ['New Product' + ' saved!']})
    # if a GET (or any other method) we'll create a blank form
    else:
        product_form = ProductForm()

        return render(request, 'main.html', {'product_form': product_form})


def mimic_purchase():
    pass


class Transactions:
    pass