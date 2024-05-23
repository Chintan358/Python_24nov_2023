from django.shortcuts import render,HttpResponse
import requests
import random
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
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
    message = '<h1>Hello</h1>'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['chintan.tops@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("mail sent")


def email_attach(request):

    subject = 'welcome to GFG world'
    message = f'Hi , testing mail....'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['chintan.tops@gmail.com']
   
    user =  EmailMessage(body=message,from_email=email_from,to=recipient_list,subject=subject)
    filepath = settings.BASE_DIR/'index.html'
    print(filepath)
    user.attach_file(filepath)
    user.send()
   
    return HttpResponse("mail sent")