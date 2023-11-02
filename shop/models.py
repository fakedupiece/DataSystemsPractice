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
    address = models.ManyToManyField(Address)

class OrderPayment(models.Model):
    card_number = models.IntegerField()
    txn_id = models.IntegerField()
    order = models.ManyToManyField(Order)
    billingAddress = models.ManyToManyField(BillingAddress)

class Product(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return "name: " + self.name + ", product ID:" + str(self.pk)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True, related_name='order_items', related_query_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    def __str__(self):
        return "name: " + self.product.name + ", product ID:" + str(self.product.pk)
# Product.item_features = models.ManyToManyField(OrderItem)

