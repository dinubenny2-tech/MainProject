from django.urls import path,include
from User import views
app_name="User"
urlpatterns = [
  path('myprofile/',views.myprofile,name="myprofile"), 
  path('editprofile/',views.editprofile,name="editprofile"),
  path('changepassword/',views.changepassword,name="changepassword"),   
  path('HomePage/',views.HomePage,name='HomePage'),  
  path('complaint/',views.complaint,name='complaint'),  
  # path('viewsc/',views.viewsc,name="viewsc"),
  path('request/',views.request,name="request"),
  path('myrequest/',views.myrequest,name="myrequest"),
  path('upload/<int:id>',views.upload,name="upload"),
  path('viewform/<int:id>',views.viewform,name='viewform'),

]