from django.db import models
from user.models import user

class Products(models.Model):
    car = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=100, blank=True)
    image = models.URLField(blank=True)
    exiting = models.BooleanField(default=True)
    productid = models.CharField(max_length=200, blank=True)
    logoimage = models.URLField(blank=True)
    right = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
    color = models.BooleanField(default=False)

    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'



class TopSells(models.Model):
    title = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    image = models.URLField(blank=True)
    exiting = models.BooleanField(default=True)
    car = models.CharField(max_length=200, blank=True)
    logoimage = models.URLField(blank=True)
    brand = models.CharField(max_length=400, blank=True)
    productid = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Topsell'
        verbose_name_plural = 'Topsells'


class Mainproduct(models.Model):
    title = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    image = models.URLField(blank=True)
    exiting = models.BooleanField(default=True)
    car = models.CharField(max_length=200, blank=True)
    logoimage = models.URLField(blank=True)
    brand = models.CharField(max_length=400, blank=True)
    productid = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'mainproduct'
        verbose_name_plural = 'mainproducts' 



class Separ(models.Model):
    title = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    image = models.URLField(blank=True)
    exiting = models.BooleanField(default=True)
    car = models.CharField(max_length=200, blank=True)
    logoimage = models.URLField(blank=True)
    brand = models.CharField(max_length=400, blank=True)
    productid = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'separ'
        verbose_name_plural = 'separs'



class headlight(models.Model):
    title = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    image = models.URLField(blank=True)
    exiting = models.BooleanField(default=True)
    car = models.CharField(max_length=200, blank=True)
    logoimage = models.URLField(blank=True)
    brand = models.CharField(max_length=400, blank=True)
    productid = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'headlight'
        verbose_name_plural = 'headlights'




class radiator(models.Model):
    title = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    image = models.URLField(blank=True)
    exiting = models.BooleanField(default=True)
    car = models.CharField(max_length=200, blank=True)
    logoimage = models.URLField(blank=True)
    brand = models.CharField(max_length=400, blank=True)
    productid = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'radiator'
        verbose_name_plural = 'radiators'




class lent(models.Model):
    title = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    image = models.URLField(blank=True)
    exiting = models.BooleanField(default=True)
    car = models.CharField(max_length=200, blank=True)
    logoimage = models.URLField(blank=True)
    brand = models.CharField(max_length=400, blank=True)
    productid = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'lent'
        verbose_name_plural = 'lents'


class Order(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.CharField(max_length=100, blank=True)
    paymentmethod = models.CharField(max_length=200, blank=True)
    totalprice = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now=True)
    isDelivered = models.BooleanField(default=False)
    deliveredat = models.DateTimeField(auto_now=True)
    createdat = models.DateTimeField(auto_now=True)
    orderproduct = models.TextField(max_length=1000)



class IdPay(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    transId = models.CharField(max_length=100, unique=True)
    lastStatus = models.IntegerField(blank=True, null=True)
    trackIdpay = models.IntegerField(blank=True, null=True)
    trackShaparak = models.CharField(max_length=50, blank=True, null=True)
    amountCreate = models.IntegerField(blank=True, null=True)
    amountPaid = models.IntegerField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)
    dateShaparak = models.DateTimeField(null=True, blank=True)
    dateVerify = models.DateTimeField(null=True, blank=True)
    cardNo =  models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.transId)
    


class Shippingaddress(models.Model):
    seen = models.BooleanField(default=False)
    user = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    nocode = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    capital = models.CharField(max_length=200, blank=True)



























