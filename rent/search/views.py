from django.shortcuts import render
from renthome.models import Property
from django.db.models import Q

# Create your views here.
def search(request):
    q=""
    property=None
    if(request.method=="POST"):
        q=request.POST['q']
        if q:
            property=Property.objects.filter(Q(name__icontains=q)|Q(dese__icontains=q))
    return render(request,'search.html',{'p':property,'query':q})