from django.db import models
from Admin.models import *
from ServiceCentre.models import*
from Guest.models import*

class tbl_worker(models.Model):
    worker_name=models.CharField(max_length=50)
    worker_email=models.CharField(max_length=50)
    worker_contact=models.CharField(max_length=50)
    worker_address=models.CharField(max_length=50)
    worker_photo=models.FileField(upload_to="Assets/WDocs/")
    worker_password=models.CharField(max_length=50)
    worker_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    servicecentre_id=models.ForeignKey(tbl_servicecentre,on_delete=models.CASCADE,null=True)

# Create your models here.
