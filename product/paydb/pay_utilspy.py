import requests, json
from product.models import IdPay, Order
from datetime import datetime, timezone
from django.utils.timezone import make_aware
from product.paydb.idpaystatus import IDPAY_STATUS




IDPAY_HEADER = {
    'Content-Type':'application/json',
    'X-API-KEY':'39831240-7573-435e-a4d9-e8867f4d56c8',
    'X-SANDBOX':'1'
}


def idpaycreatepay(order):
    body = {
        'order_id' : str(order._id),
        'amount': int(order.totalprice * 10),
        'callback' : 'http://jahanyadak.iran.liara.run/api/result/',
    }
        
    
    response = requests.post(
        'https://api.idpay.ir/v1.1/payment',
        data= json.dumps(body),
        headers = IDPAY_HEADER
    )


    return response


def idpaycreatedb(order, id):
    try:
        idpay = IdPay.objects.create(
            order = order,
            transId = id,
            lastStatus = 0,
            amountCreate = (order.totalprice * 10)
        )

        return True
    except:
        return False
    


def idpayupdatedb(pay_entry, lastStatus, trackidpay):
    try:
        pay_entry.lastStatus = lastStatus
        pay_entry.trackIdpay = trackidpay
        pay_entry.save()
        return True
    except:
        return False
    

def idpayverify(order_id, transid):
    body = {
        'id' : str(transid),
        'order_id' : str(order_id)
    }
    response = requests.post(
        'https://api.idpay.ir/v1.1/payment/verify',
        data= json.dumps(body),
        headers= IDPAY_HEADER
    )
    return response


def idpaycompletedb(data):
    try:
        pay = IdPay.objects.get(transId=data['id'])
        pay.lastStatus = data['status']
        pay.trackIdpay = data['track_id']
        pay.trackShaparak = data['payment']['track_id']
        pay.amountPaid = data['payment']['amount']
        pay.cardNo = data['payment']['card_no']
        
        pay.dateShaparak = make_aware(datetime.fromtimestamp(int(data['payment']['date'])), timezone.utc) 
        pay.dateVerify = make_aware(datetime.fromtimestamp(int(data['verify']['date'])), timezone.utc) 
        pay.save()
        order = Order.objects.get(_id=data['order_id'])
        order.is_paid = True
        order.paid_at = make_aware(datetime.fromtimestamp(int(data['payment']['date'])), timezone.utc) 
        order.save()
        return True
    except:
        return False
    


def makeinquirypayment(lastStatus, order_id, track_id):
    msg = ""
    succsess = False
    if lastStatus == 100 or lastStatus == 101 or lastStatus == 200:
        succsess = True
        for k,v in IDPAY_STATUS.items():
            if k == lastStatus:
                msg = v
        if msg == "":
            msg = "transaction status unknown"

        return {
            'message': msg,
            'success': succsess,
            'status': lastStatus,
            'order_id': order_id,
            'track_id': track_id,
        }
    


def inquiryidpay(transId, order_id):
    body = {
        'id': str(transId),
        'order_id': str(order_id)
    }

    response = requests.post(
        'https://api.idpay.ir/v1.1/payment/inquiry',
        data= json.dumps(body),
        headers=IDPAY_HEADER
    )
    return response
