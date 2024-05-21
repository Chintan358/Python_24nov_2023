from django.shortcuts import render,HttpResponse
import requests
import random
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def sms(request):

    otp = random.randint(0000,9999)
    url = "https://www.fast2sms.com/dev/bulkV2"


    # querystring = {"authorization":"","variables_values":otp,"route":"otp","numbers":"8200386261"}

    querystring = {"authorization":"","message":"This is test message","language":"english","route":"q","numbers":"9904023817"}


    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)


    return HttpResponse(response.text)

def email(request):


    subject = 'welcome to GFG world'
    message = f'Hi , testing mail....'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['chintan.tops@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("mail sent")