
from django.urls import path,include
from Guest import views
app_name="Guest"
urlpatterns = [
  path('userregistration/',views.userregistration,name="userregistration"), 
  path('login/',views.login,name="login"),  
  path('ajaxplace/',views.ajaxplace, name='ajaxplace'),
  path('scregistration/',views.scregistration,name="scregistration"),
  path('index/',views.index,name="index"),
  
   
     
]