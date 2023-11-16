# from django.db import models
#

# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     shippingAddress = models.OneToOneField("Address", on_delete=models.PROTECT)
#

# class BillingAddress(models.Model):
#     customer = models.ManyToManyField("Customer")
#     address = models.ManyToManyField(Address)
#
# class OrderPayment(models.Model):
#     card_number = models.IntegerField()
#     txn_id = models.IntegerField()
#     order = models.ManyToManyField(Order)
#     billingAddress = models.ManyToManyField(BillingAddress)
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True,
#                               related_name='order_items', related_query_name='order_item')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     price = models.IntegerField()
#     def __str__(self):
#         return "name: " + self.product.name + ", product ID:" + str(self.product.pk)
# # Product.item_features = models.ManyToManyField(OrderItem)

from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    postcode = models.SmallIntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=100)

class BillingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shippingAddress = models.OneToOneField("Address", on_delete=models.CASCADE)

class OrderPayment(models.Model):
    card_number = models.BigIntegerField()
    txn_id = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    billingAddress = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "name: " + self.name + ", product ID:" + str(self.pk)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True,
                              related_name='order_items', related_query_name='order_item')
    price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return "name: " + self.product.name + ", product ID:" + str(self.product.pk)
# Product.item_features = models.ManyToManyField(OrderItem)
