from django.shortcuts import render
import razorpay
from django.http import JsonResponse
# Create your views here.
def pay(request):

    amt = request.GET.get("amt")
    amount = int(amt)*100
    client = razorpay.Client(auth=("rzp_test_2xdaXtpM3wSbRh", "zLAly9UBfnrocQ3IkBGdHA7M"))

    data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }

    payment = client.order.create(data=data)

    print(payment)

    return JsonResponse(payment)

def payment(request):
     return render(request,"payment.html")