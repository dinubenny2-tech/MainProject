from django.urls import path,include
from Worker import views
app_name="Worker"
urlpatterns = [
    path('HomePage/',views.HomePage,name='HomePage'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('viewwork/',views.viewwork,name='viewwork'),
    path('join/<int:aid>',views.join,name="join"),
    path('myworks/',views.myworks,name='myworks'),
    path('replacement/<int:rid>',views.replacement,name="replacement"),
    path('repair/<int:aid>',views.repair,name="repair"),
    path('viewfile/<int:id>',views.viewfile,name="viewfile"),
    path('todate/<int:id>',views.todate,name="todate"),
    path('form/<int:id>',views.form,name='form'),
    path('assessment/',views.assessment,name='assessment'),
]