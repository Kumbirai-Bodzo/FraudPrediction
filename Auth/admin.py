from django.contrib import admin
from .auto_create_super_user import *
# Register your models here.
try:

    admin.site.site_title = "Fraud Prediction"

    admin.site.site_header = "Fraud Prediction"
    admin.site.index_title = "App List"
except Exception as e:
    print(e)
    pass
