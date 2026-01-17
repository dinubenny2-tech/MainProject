from django.db import models
from User.models import *

class tbl_replacement(models.Model):
    replacement_code=models.IntegerField(null=True)
    replacement_sino=models.IntegerField(null=True)
    replacement_qty=models.IntegerField(null=True)
    replacement_voltage=models.IntegerField(null=True)
    replacement_ampere=models.IntegerField(null=True)
    replacement_app=models.CharField(max_length=50)
    replacement_period=models.IntegerField(null=True)
    replacement_complaint=models.CharField(max_length=50)
    replacement_status=models.CharField(max_length=50)
    request=models.ForeignKey(tbl_request,on_delete=models.CASCADE)
    
# Create your models here.
