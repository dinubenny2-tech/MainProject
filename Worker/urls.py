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
    path('risk_assessment/<int:id>/', views.risk_assessment, name='risk_assessment'),
    path('complete_work/<int:id>/', views.complete_work, name='complete_work'),
    path('start_work/<int:id>/', views.start_work, name='start_work'),
    path('end_work/<int:id>/', views.end_work, name='end_work'),
    path('cancel_work/<int:id>/', views.cancel_work, name='cancel_work'),
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    
    

]