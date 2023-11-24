from django.contrib import admin
from .models import Products, TopSells, radiator, lent, Separ, headlight, Order, IdPay, Mainproduct, Shippingaddress

@admin.register(Products)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'exiting', 'car']


@admin.register(TopSells)

class topselladmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'image', 'exiting', 'car']




@admin.register(Separ)

class Separadmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'image', 'exiting', 'car']



@admin.register(radiator)

class radiatoradmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'image', 'exiting', 'car']




@admin.register(lent)

class lentAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'image', 'exiting', 'car']




@admin.register(headlight)

class headlightadmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'image', 'exiting', 'car']



@admin.register(Order)

class orderadmin(admin.ModelAdmin):
    list_display = ['_id', 'totalprice']


admin.site.register(IdPay)



@admin.register(Mainproduct)

class mainproductadmin(admin.ModelAdmin):
  list_display = ['title', 'price', 'image', 'exiting', 'car']

@admin.register(Shippingaddress)

class shippingadmin(admin.ModelAdmin):
    list_display = ['nocode', 'address', 'city', 'capital', 'id', 'user', 'seen']
    search_fields = ['user']

    

















