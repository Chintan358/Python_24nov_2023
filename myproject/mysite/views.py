from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("""<h1>Index</h1>
                        
    #                     <a href='about'>python</a>
    #                     """)
    return render(request,'index.html')

def home(request):
     # conext = {"data":"Hello python"}

     std = [{"name":"Maulik","email":"maulik@gmail.com", "phone":"9685748596"},{"name":"Priyansh","email":"priyansh@gmail.com", "phone":"9685748596"},{"name":"Akshay","email":"akshay@gmail.com", "phone":"9685748566"}]
     
     return render(request,'home.html',{'stddata':std})

def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')
