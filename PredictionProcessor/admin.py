from django.contrib import admin
# from .models import Message
# # Register your models here.
# class MessageAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'sequence', 'date_created']


# admin.site.register(Message,MessageAdmin)
from django import template

from PredictionProcessor.models import Reports
from import_export.admin import ImportExportModelAdmin

class ReportsAdmin(ImportExportModelAdmin):
    list_display =  ['id','batch_no','transaction_id','probability_fradulent','date_created']
    list_filter = ['date_created','batch_no']
    ordering =['batch_no','-probability_fradulent']
    
register = template.Library()
admin.site.register(Reports,ReportsAdmin)
@register.filter()
def to_int(value):
    return int(value)