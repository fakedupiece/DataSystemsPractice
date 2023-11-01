from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Address(models.Model):
    address = models.TextField()

Order.shippingAddress = models.OneToOneField(Address, on_delete=models.PROTECT)

class BillingAddress(models.Model):
    customer = models.ManyToManyField(Customer)

class OrderPayment(models.Model):
    card_number = models.IntegerField()
    txn_id = models.IntegerField()
    order = models.ManyToManyField(Order)
    billingAddress = models.ManyToManyField(BillingAddress)

class Product(models.Model):
    name = models.CharField(max_length=200)

class OrderItem(models.Model):
    price = models.IntegerField()
    order = models.ManyToManyField(Order)
    product = models.ManyToManyField(Product)





