from django.contrib import admin
from book.models import Booking,Order,Account

# Register your models here.
admin.site.register(Booking)
admin.site.register(Order)
admin.site.register(Account)