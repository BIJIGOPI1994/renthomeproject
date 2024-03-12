from book.models import Booking

def propertycount(request):
    item_count=0
    if request.user.is_authenticated:
        u=request.user
        try:
            b=Booking.objects.filter(user=u)
            for i in b:
                item_count=item_count+i.quantity
        except:
            item_count=0
    return {'count':item_count}            