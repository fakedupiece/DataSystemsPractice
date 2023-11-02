from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomerForm, ProductForm, UpdatePriceForm, AddToBasketForm
from .models import Customer, Address, Product, OrderItem, BillingAddress, Order, OrderPayment


def index_shop(request):
    customer_form = CustomerForm()
    product_form = ProductForm()
    update_price_form = UpdatePriceForm()
    add_to_basket_form = AddToBasketForm()
    return render(request, 'main.html', {'customer_form': customer_form,
                                         'product_form': product_form,
                                         'update_price_form': update_price_form,
                                         'add_to_basket_form':add_to_basket_form})


def create_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            name = customer_form.cleaned_data['name']
            customer = Customer(name=name)
            customer.save()
            return render(request, "model_saved.html", {'messages': 'New Customer saved!'})

def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            name = product_form.cleaned_data['name']
            price = product_form.cleaned_data['price']
            product = Product(name=name)
            product.save()
            item = OrderItem(order=None,product=product, price=price)
            item.save()
            return render(request, "model_saved.html", {'messages': 'New Product saved!'})

def update_price(request):
    if request.method == 'POST':
        update_price_form = UpdatePriceForm(request.POST)
        if update_price_form.is_valid():
            # your_product = update_price_form.cleaned_data['your_product_id_and_name']
            your_product_id = update_price_form.cleaned_data['your_product_ID']
            new_price = update_price_form.cleaned_data['new_price']

            product = get_object_or_404(Product, pk=your_product_id)

            item = OrderItem.objects.filter(product__exact= product.pk).first()
            if item:
                item.price = new_price # TODO: learn objects.update()
                item.save()
                return render(request, "model_saved.html", {'messages': 'Price Updated!'})


def add_to_basket(request):
    if request.method == 'POST':
        add_to_basket_form = AddToBasketForm(request.POST)
        if add_to_basket_form.is_valid():
            product_id = add_to_basket_form.cleaned_data['product_id'].id
            quantity = add_to_basket_form.cleaned_data['quantity']

            product = Product.objects.get(pk=product_id)

            # Find an incomplete order by looking for orders with associated items
            orders_with_items = OrderItem.objects.values_list('order', flat=True).distinct()
            incomplete_orders = Order.objects.exclude(id_in=orders_with_items)

            if incomplete_orders.exists():
                current_order = incomplete_orders.first()
            else:
                current_order = Order.objects.create()

            OrderItem.objects.create(order=current_order, product=product, price=product.price, quantity=quantity)

            return redirect('basket')  # Redirect to the basket view after adding the item


def basket(request):
    orders_with_items = Order.objects.filter(id__in=OrderItem.objects.values('order_id').distinct())

    return render(request, 'shopping_basket.html', {'orders_with_items': orders_with_items})

def mimic_purchase():
    pass


class Transactions:
    pass