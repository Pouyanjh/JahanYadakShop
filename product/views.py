from django.shortcuts import render
from .serializer import ProductSerializer, Topsellsserializer, separserializer, headlightserializer, lentserializer, radiatorserializer, mainproductserializer, orderserializer, shippingserializer
from .models import Products, TopSells, lent, radiator, Separ, headlight, Order, IdPay, Mainproduct, Shippingaddress
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from product.paydb.pay_utilspy import idpaycreatedb, idpaycreatepay, idpayupdatedb, idpayverify, idpaycompletedb, makeinquirypayment, inquiryidpay
from django.http import HttpResponseRedirect


class GetListProduct(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

class mainproduct(APIView):
    def get(self, request):
        main = Mainproduct.objects.all()
        serializer = mainproductserializer(main, many=True)
        return Response(serializer.data)



class Getproduct(APIView):

    def get(self, request, brand):
        comment = Products.objects.get(brand=brand)
        serializer = ProductSerializer(comment)
        return Response(serializer.data)



class Topsellsviews(APIView):
    def get(self, request):
        topsellsproduct = TopSells.objects.all()
        serializer = Topsellsserializer(topsellsproduct, many=True)
        return Response(serializer.data)



class Separview(APIView):
    def get(self, request):
        separsproduct = Separ.objects.all()
        serializer = separserializer(separsproduct, many=True)
        return Response(serializer.data)


class Radiatorview(APIView):
    def get(self, request):
        radiatorsproduct = radiator.objects.all()
        serializer = radiatorserializer(radiatorsproduct, many=True)
        return Response(serializer.data)


class Lentview(APIView):
    def get(self, request):
        lentsproduct = lent.objects.all()
        serializer = lentserializer(lentsproduct, many=True)
        return Response(serializer.data)


class Headlightview(APIView):
    def get(self, request):
        headlightsproduct = headlight.objects.all()
        serializer = headlightserializer(headlightsproduct, many=True)
        return Response(serializer.data)



class Getdetailproduct(APIView):
    def get(self, request, productid):
        detail = Products.objects.get(productid=productid)
        serializer = ProductSerializer(detail)
        return Response(serializer.data)
        



@api_view(['POST'])
def addorderview(request):
    # user = request.user
    data = request.data
    order = Order.objects.create(
        user = data['user'],
        orderproduct = data['orderitem'],
        paymentmethod = data['payment'],
        totalprice = data['totalprice'],
    )
    serializer = orderserializer(order, many=False)
    return Response(serializer.data)

    

@api_view(['GET'])
def payorder(request, pk):

    try:
        order = Order.objects.get(_id=pk)
    except Order.DoesNotExist:
        return Response({'detail': 'order not found !'}, status=status.HTTP_404_NOT_FOUND)
    

    else:
        if order.is_paid:
            return Response({'detail': 'order already paid !'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                response = idpaycreatepay(order)
            except:
                return Response({'detail': 'the id pay server connection was established !'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                if(str(response.status_code).startswith('2')):
                    resjson = response.json()
                    if(idpaycreatedb(order, resjson['id'])):

                        return Response(resjson, status=status.HTTP_200_OK)
                    else:
                        return Response({'detail': 'db error!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    


@api_view(['POST'])
def Idpaycallback(request):
    data = request.data

    try:
        callbackpaystatus = data['status']
        trackidpay = data['track_id']
        transid = data['id']
        order_id = data['order_id']

        order = Order.objects.get(_id=order_id)
        pay_entry = IdPay.objects.get(transId=transid, order=order)
        if order.is_paid:
            return HttpResponseRedirect(f"https://jahanpartshop.ir/payresult/{trackidpay}/{order_id}/{transid}?db=Null")
    except:
        return Response({'detail': 'transaction processing error!'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        #transactionn verify
        if (str(callbackpaystatus) == '10'):
            try:
                resonse = idpayverify(order_id, transid)
            except:
                dbstatus = idpayupdatedb(pay_entry, 500, trackidpay)
                return HttpResponseRedirect(f"https://jahanpartshop.ir/payresult/{trackidpay}/{order_id}/{transid}?db={dbstatus}")
            else:
                if(str(resonse.status_code).startswith('2')):
                    resjson = resonse.json()
                    dbstatus = idpaycompletedb(resjson)
                    return HttpResponseRedirect(f"https://jahanpartshop.ir/payresult/{trackidpay}/{order_id}/{transid}?db={dbstatus}")
                else:
                    dbstatus = idpayupdatedb(pay_entry, 400, trackidpay)
                    return HttpResponseRedirect(f"https://jahanpartshop.ir/payresult/{trackidpay}/{order_id}/{transid}?db={dbstatus}")
                
        else:
            dbstatus = idpayupdatedb(pay_entry, callbackpaystatus, trackidpay)
            return HttpResponseRedirect(f"https://jahanpartshop.ir/payresult/{trackidpay}/{order_id}/{transid}?db={dbstatus}")
        
@api_view(['POST'])
def inquirypay(request, pk):
    try:
        data = request.data
        # user = request.user
        transId = data['transId']
        track_id = data['track_id']
        order = Order.objects.get(_id=pk)
        pay_entry = IdPay.objects.get(transId=transId)
    except:
        return Response({'detail': 'transaction details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    else:
        if(pay_entry.trackIdpay and pay_entry.lastStatus != 0):
            if(str(pay_entry.trackIdpay) == str(track_id)):
                return Response(makeinquirypayment(pay_entry.lastStatus, order._id, track_id), status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'transaction details are not valid'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            # TRANSACTION INQUIRY
            try:
                response = inquiryidpay(transId, order._id)
            except:
                if(idpayupdatedb(pay_entry, 500, track_id)):
                    return Response(inquirypay(500, order._id, track_id), status=status.HTTP_200_OK)
                
                else:
                    return Response({'detail': 'registration error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                if(str(response.status_code).startswith('2')):
                    try:
                        resjson = response.json()
                        lastStatus = resjson['status']
                    except:
                        if(idpayupdatedb(pay_entry, 500, track_id)):
                            return Response(makeinquirypayment(500, order._id, track_id), status=status.HTTP_200_OK)
                        else:
                            return Response({'detail': 'registration errors'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        
                    else:
                        if(lastStatus == 100 or lastStatus == 101 or lastStatus == 200):
                            if(idpaycompletedb(resjson)):
                                return Response(makeinquirypayment(500, order._id, track_id), status=status.HTTP_200_OK)
                            else:
                                return Response({'detail': 'registration payment confirmed error!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:
                            if(idpayupdatedb(pay_entry, lastStatus, track_id)):
                                return Response(makeinquirypayment(lastStatus, order._id, track_id), status=status.HTTP_200_OK)
                            else:
                                return Response({'detail': 'payment is not complete'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                else:
                    if(idpayupdatedb(pay_entry, 500, track_id)):
                        return Response(makeinquirypayment(500, order._id, track_id), status=status.HTTP_200_OK)
                    else:
                        return Response({'detail': 'registration errors'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    

@api_view(['POST'])
def shippingadd(request):
    data = request.data
    shipping = Shippingaddress.objects.create(
       nocode = data['nocode'],
        user = data['user'],
        address = data['address'],
        city = data['city'],
        capital = data['capital']
    )
    serializer = shippingserializer(shipping)
    return Response(serializer.data)






class getdetailshipping(APIView):
    def get(self, request, id):
        detail = Shippingaddress.objects.get(id=id)
        serializer = shippingserializer(detail)
        return Response(serializer.data)











