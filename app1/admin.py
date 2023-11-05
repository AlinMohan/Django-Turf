from django.contrib import admin
from app1.models import User,Booking

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Place','Phone','Email','Username','Password')

admin.site.register(User,UserAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Place','Phone','Game','Date_Time')

admin.site.register(Booking,BookingAdmin)