from django.shortcuts import render,redirect
from renthome.models import Category,Property
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse







# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def renthome(request):
    return render(request,'renthome.html')

def rentflat(request):
    return render(request,'rentflat.html')
# def blog(request):
#     return render(request,'blog.html')






def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproperty(request,p):
    c=Category.objects.get(name=p)
    pro=Property.objects.filter(category=c)
    return render(request,'property.html',{'c':c,'p':pro})

def details(request,p):
    pro=Property.objects.get(name=p)
    return render(request,'details.html',{'p':pro})

def contact(request):
    return render(request,'contact.html')


def user_login(request):
    if(request.method=="POST"):
        name=request.POST['u']
        pass1=request.POST['p']
        user=authenticate(username=name,password=pass1)
        if user:
            login(request,user)
            return redirect('renthome:allcat')
        else:
            messages.error(request,"Invalid credentails")
    return render(request,'login.html')

    
    
def register(request):
    if(request.method=="POST"):
        u=request.POST["u"]
        p=request.POST["p"]
        cp=request.POST["cp"]
        e=request.POST["e"]
       
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e)
            return redirect("renthome:user_login")
        else:
            return redirect("password not matching")
    return render(request,'register.html')  

@login_required
def user_logout(request):
    logout(request)  
    return redirect('renthome:index')

