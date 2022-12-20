from django.contrib import admin
from . models import ConsertModel
from . models import LocationModel
from . models import TimeModel
from . models import TicketModel


admin.site.register(ConsertModel)
admin.site.register(LocationModel)
admin.site.register(TimeModel)
admin.site.register(TicketModel)

