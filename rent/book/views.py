from django.shortcuts import render,redirect
# from django.conf import settings
from book.models import Booking
from renthome.models import Property
from book.models import Account
from django.contrib.auth.decorators import login_required


# Create your views here.
def bookview(request):
    total=0
    u=request.user
    try:
        b=Booking.objects.filter(user=u)
        for i in b:
            total+=i.quantity*i.property.bookingprice
    except:
        pass        
    
    return render(request,'book.html',{'b':b,'total':total})

# @login_required
def addtobook(request,p):
    
    property=Property.objects.get(name=p)
    u=request.user
    try:
        b=Booking.objects.get(user=u,property=property)
        if(b.quantity<b.property.stock):
            b.quantity+=1
        b.save()
    except:
        b=Booking.objects.create(property=property,user=u,quantity=1)
        b.save()

    return redirect('book:bookview')

def book_remove(request,p):
    p=Property.objects.get(name=p)
    u=request.user
    try:
        b=Booking.objects.get(user=u,property=p)
        if b.quantity>1:
            b.quantity-=1
            
            b.save()
        else:
            b.delete()    
    except:
        pass
    return redirect('book:bookview')        

def full_remove(request,p):
    p=Property.objects.get(name=p)
    u=request.user
    try:
        b=Booking.objects.get(user=u,property=p)
        b.delete()
            
    except:
        pass
    return redirect('book:bookview')  
          
def orderform(request):
    if(request.method=='POST'):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']
        u=request.user
        b=Booking.objects.filter(user=u)
        
        total=0
        for i in b:
            total+=i.quantity*i.property.bookingprice
            
            
        ac=Account.objects.get(acctnum=n)
        if(ac.amount>=total):
            ac.amount=ac.amount-total 
            ac.save()
        else:
            pass     
                 
    return render(request,'orderform.html')                 
            