from django.urls import path,include
from ServiceCentre import views
app_name="ServiceCentre"
urlpatterns = [
    path('HomePage/',views.HomePage,name='HomePage'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('wregistration/',views.wregistration,name="wregistration"),
    path('viewrequest/',views.viewrequest,name="viewrequest"),
    path('viewworker/',views.viewworker,name="viewworker"),
]