from rest_framework import serializers
from .models import Products, TopSells, Separ, lent, headlight, radiator, Mainproduct, Order, Shippingaddress

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = (
            'title', 'price', 'image', 'exiting', 'car', 'productid', 'logoimage', 'color', 'right', 'left'
        )


class Topsellsserializer(serializers.ModelSerializer):

    class Meta:
        model = TopSells
        fields = (
            'title', 'price', 'image', 'exiting', 'car', 'logoimage', 'productid'
        )


class separserializer(serializers.ModelSerializer):

    class Meta:
        model = Separ
        fields = (
            'title', 'price', 'image', 'exiting', 'car', 'logoimage', 'productid'
        )


class headlightserializer(serializers.ModelSerializer):

    class Meta:
        model = headlight
        fields = (
            'title', 'price', 'image', 'exiting', 'car', 'logoimage', 'productid'
        )



class lentserializer(serializers.ModelSerializer):

    class Meta:
        model = lent
        fields = (
            'title', 'price', 'image', 'exiting', 'car', 'logoimage', 'productid'
        )



class radiatorserializer(serializers.ModelSerializer):

    class Meta:
        model = radiator
        fields = (
            'title', 'price', 'image', 'exiting', 'car', 'logoimage', 'productid'
        )

class mainproductserializer(serializers.ModelSerializer):

    class Meta:
        model = Mainproduct
        fields = (
            'title', 'price', 'image', 'exiting', 'car', 'logoimage', 'productid'
        )


class orderserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = (
            '_id', 'totalprice', 'paymentmethod', 'orderproduct', 'user'
        )


class shippingserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shippingaddress
        fields = (
            'nocode', 'city', 'capital', 'address', 'user', 'id'
        )









