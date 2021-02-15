from django.contrib import admin
from .models import MpesaPayment,MpesaCalls,MpesaCallBacks


admin.site.register(MpesaPayment)
admin.site.register(MpesaCalls)
admin.site.register(MpesaCallBacks)