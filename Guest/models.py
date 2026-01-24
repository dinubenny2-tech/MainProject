from django.db import models
from Admin.models import *

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_mobile=models.CharField(null=True)
    user_address=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_photo = models.FileField(upload_to="Assets/UserDocs/")
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
class tbl_servicecentre(models.Model):
    servicecentre_name=models.CharField(max_length=50)
    servicecentre_details=models.CharField(max_length=50)
    servicecentre_address=models.CharField(max_length=50)
    servicecentre_photo=models.FileField(upload_to="Assets/ScDocs/")
    servicecentre_proof=models.FileField(upload_to="Assets/ScDocs/")
    servicecentre_contact=models.CharField(max_length=50)
    servicecentre_email=models.CharField(max_length=50)
    servicecentre_password=models.CharField(max_length=50)
    servicecentre_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)





