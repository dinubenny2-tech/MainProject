
from django.urls import path,include
from Admin import views
app_name="Admin"
urlpatterns = [
     path('HomePage/',views.HomePage,name="HomePage"), 
     path('AdminRegistration/',views.AdminRegistration,name="AdminRegistration"), 
     path('district/',views.district,name="district"),
     path('category/',views.category,name="category"),
     path('place/',views.place,name="place"),
     path('delplace/<int:id>',views.delplace,name="delplace"),
     path('editplace/<int:id>',views.editplace,name="editplace"),
     path('subcategory/',views.subcategory,name="subcategory"),
     path('delsubcategory/<int:id>',views.delsubcategory,name="delsubcategory"),
     path('editsubcategory/<int:id>',views.editsubcategory,name="editsubcategory"),
     path('deldistrict/<int:id>',views.deldistrict,name="deldistrict"),
     path('delcategory/<int:id>',views.delcategory,name="delcategory"),
     path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),
     path('editcategory/<int:id>',views.editcategory,name="editcategory"),
     path('deladmin/<int:id>',views.deladmin,name="deladmin"),
     path('editadmin/<int:id>',views.editadmin,name="editadmin"),
     path('userlist/',views.userlist,name="userlist"),
     path('sclist/',views.sclist,name="sclist"),
     path('scverification/',views.scverification,name="scverification"),
     path('scaccept/<int:aid>',views.scaccept,name="scaccept"),
     path('screject/<int:rid>',views.screject,name="screject"),
     path('viewrequest/',views.viewrequest,name="viewrequest"),
     path('accept/<int:aid>',views.accept,name="accept"),
     path('reject/<int:rid>',views.reject,name="reject"),
     path('viewsc/<int:rid>',views.viewsc,name="viewsc"),
     path('assign/<int:sid>/<int:rid>/',views.assign,name="assign"),
     path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
     path('reply/<int:id>',views.reply,name="reply"),

]