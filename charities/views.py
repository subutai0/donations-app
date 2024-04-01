from django.shortcuts import render
from .models import Charity
from django.conf import settings
from paypalrestsdk import Payment
import paypalrestsdk

def charity_list(request):
    charities = Charity.objects.all()
    return render(request, 'charities/charity_list.html', {'charities': charities})

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def paypal_payment(request, donation_id):
    donation = Charity.objects.get(pk=donation_id)
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": f"{request.build_absolute_uri('/')}/payment/execute/",
            "cancel_url": f"{request.build_absolute_uri('/')}/payment/cancel/",
        },
        "transactions": [{
            "amount": {
                "total": str(donation.amount),
                "currency": "USD",
            },
            "description": f"Donation to {donation.charity.name}",
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == 'approval_url':
                return (link.href)
    else:
        return render(request, 'error.html', {'error': payment.error})
    
def payment_execute(request):
    payment = paypalrestsdk.Payment.find(request.GET['paymentId'])
    if payment.execute({"payer_id": request.GET['PayerID']}):
        return render(request, 'success.html')
    else:
        return render(request, 'error.html', {'error': payment.error})

def payment_cancel(request):
    return render(request, 'cancel.html')



