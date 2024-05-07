from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
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
            print(d.total)
            print(rank)
            break;
        rank = rank+1
            



    return render(request,"card.html",{"sdata":data,"pdata":data[0].student,"total":sum,"rank":rank})