from django.db import models
from renthome.models import Property
from django.contrib.auth.models import User
# Create your models here.
class Booking(models.Model):
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    data_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.property.name
    def suntotal(self):
        return self.quantity*self.property.price
    
class  Order(models.Model):
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_items=models.IntegerField() 
    address=models.TextField()
    order_status=models.CharField(max_length=20,default="pending")
    date_ordered=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
class Account(models.Model):
    acctnum=models.CharField(max_length=20)    
    accttype=models.CharField(max_length=20)
    amount=models.IntegerField()
    def __str__(self):
        return self.acctnum
    