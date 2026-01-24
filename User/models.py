from django.db import models
from Guest.models import *
from ServiceCentre.models import *
class tbl_request(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_todate=models.DateField(null=True)
    request_details=models.CharField(max_length=50)
    request_emdetails=models.CharField(max_length=50,null=True)
    request_status=models.IntegerField(default=0)
    request_amount=models.CharField(max_length=50)
    request_emergency=models.IntegerField(null=True)
    request_starttime=models.DateTimeField(null=True)
    request_endtime=models.DateTimeField(null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    servicecentre=models.ForeignKey(tbl_servicecentre,on_delete=models.CASCADE,null=True)
    worker=models.ForeignKey(tbl_worker,on_delete=models.CASCADE,null=True)
    product_photo=models.FileField(upload_to="Assets/UDocs/",null=True)
    product_bill=models.FileField(upload_to="Assets/UDocs/",null=True)
class tbl_complaint(models.Model):
    complaint_title=models.CharField(null=True)
    complaint_content=models.CharField(null=True)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(null=True)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
class tbl_rating(models.Model):
    rating_content=models.CharField(null=True)
    rating_value=models.CharField(null=True)
    rating_datetime=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    servicecentre=models.ForeignKey(tbl_servicecentre,on_delete=models.CASCADE)
# Create your models here.

