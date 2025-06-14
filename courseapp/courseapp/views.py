from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')   # You must have templates/index.html

def aboutus(request):
    return render(request,'base.html')  

def course_detail(request, course_id):
    return HttpResponse(course_id)

def account(request):
    return render(request, 'account.html')  

def faqs(request):
    return render(request,'faqs.html')

def contact(request):
    return render(request, 'contact.html')

def instructors(request):
    return render(request, 'instructors.html')

def cart (request):
    return render(request,'cart.html')

def priceplan(request):
    return render(request,'priceplan.html')

def wishlist(request):
    return render(request,'wishlist.html')

def course(request):
    return render(request,'course.html')

# def xyz(request):
#     return HttpResponse("this is XYZ page")  # This is just a exmplae to show, is we want to see a page with only text , write this code

def userform(request):
    ans=0
    try:
        if request.method == 'POST':
         n1=int(request.POST['username'])
         n2=int(request.POST['password'])
         ans=n1 + n2 # This will print the username and password in the console
    except Exception as e:
        pass
    return render(request,'userform.html',{'output':ans})