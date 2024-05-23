from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
# Create your views here.
def index(request):

    studen_data = Student.objects.all()
    if request.GET.get('search'):
        s_data = request.GET.get('search')      
        studen_data = Student.objects.filter(name__startswith=s_data)

    
   

    paginator = Paginator(studen_data, 7)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    

    return render(request,"index.html",{"sdata":page_obj})

def marks(request,id):
    data =  SubjectMarks.objects.filter(student__studentid__student_id=id)
   
    sum = 0;
    for dt in data:
       sum = sum + dt.marks
    
    s_data  = Student.objects.annotate(total = Sum("subjectmarks__marks")).order_by("-total")
    rank = 1
    for d in s_data:
        if d.studentid.student_id == id:
            
            break;
        rank = rank+1
            


    id = data[0].student.studentid.student_id
    return render(request,"card.html",{"sdata":data,"pdata":data[0].student,"total":sum,"rank":rank,"id":id})

def mail(request,id):

    data =  SubjectMarks.objects.filter(student__studentid__student_id=id)
   
    sum = 0;
    for dt in data:
       sum = sum + dt.marks
    
    s_data  = Student.objects.annotate(total = Sum("subjectmarks__marks")).order_by("-total")
    rank = 1
    for d in s_data:
        if d.studentid.student_id == id:
            
            break;
        rank = rank+1
            

    subject = 'welcome to GFG world'
    message = '<h1>Hello</h1>'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [data[0].student.email]
    send_mail( subject, message, email_from, recipient_list )
    return redirect("index")



