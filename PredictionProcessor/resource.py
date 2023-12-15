from import_export import resources 
from .models import Reports
class ReportResource(resources.ModelResource):
     class Meta:
         model = Reports