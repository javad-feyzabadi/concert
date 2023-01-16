from django.contrib import admin
from . models import ConsertModel
from . models import LocationModel
from . models import TimeModel
from . models import TicketModel

class ConcertAdmin(admin.ModelAdmin):
    list_display = ('name' ,'singername', 'length' ,'poster')
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name' ,'address', 'phone' ,'capacity')
class TimeAdmin(admin.ModelAdmin):
    list_display = ('consert' ,'location', 'startdatetime' ,'seats','status')
class TicketAdmin(admin.ModelAdmin):
    list_display = ('profilemodel' ,'timemodel', 'name' ,'price','ticketimage')

admin.site.register(ConsertModel,ConcertAdmin)
admin.site.register(LocationModel,LocationAdmin)
admin.site.register(TimeModel,TimeAdmin)
admin.site.register(TicketModel,TicketAdmin)

