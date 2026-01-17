from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
from User.models import*
from datetime import datetime


# Create your views here.
def HomePage(request):
    if "aid" not in request.sesion:
        return redirect("Guest/Login.html")
    else:
        return render(request,"Admin/HomePage.html")

def AdminRegistration(request):
    data=tbl_admin.objects.all()
    if  request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password= request.POST.get("txt_password")
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request,'Admin/AdminRegistration.html',{'msg':"Data inserted.."})
    else:     
        return render(request,'Admin/AdminRegistration.html',{"reg":data})
def district(request):
    data=tbl_district.objects.all()
    if  request.method=="POST":
        district=request.POST.get("txt_district")
        tbl_district.objects.create(district_name=district)
        return render(request,'Admin/District.html',{'msg':'data inserted'})
    else:    
        return render(request,'Admin/District.html',{"district":data})
def category(request):
    data=tbl_category.objects.all()
    if request.method=="POST":
       category=request.POST.get("txt_category")
       tbl_category.objects.create(category_name=category)
       return render(request,'Admin/Category.html',{'msg':'data inserted'})
    else:
         return render(request,'Admin/Category.html',{"category":data})  
def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:district")
def delcategory(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:category")
def editdistrict(request,id):
    editdata=tbl_district.objects.get(id=id)
    if request.method=="POST":
        district=request.POST.get("txt_district")
        editdata.district_name=district
        editdata.save()
        return redirect("Admin:district")
    else:    
       return render(request,'Admin/District.html',{'editdata':editdata})    
def editcategory(request,id):
    editdata=tbl_category.objects.get(id=id)
    if request.method=="POST":
        category=request.POST.get("txt_category")
        editdata.category_name=category
        editdata.save()
        return redirect("Admin:category")
    else:    
       return render(request,'Admin/Category.html',{'editdata':editdata}) 
def deladmin(request,id):
    tbl_admin.objects.get(id=id).delete()
    return redirect("Admin:AdminRegistration") 
def editadmin(request,id):
    editdata=tbl_admin.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        editdata.admin_name=name
        email=request.POST.get("txt_email")
        editdata.admin_email=email
        editdata.save()
        return redirect("Admin:AdminRegistration")
    else:    
       return render(request,'Admin/AdminRegistration.html',{'editdata':editdata})    
def place(request):
    ddata=tbl_district.objects.all()
    pdata=tbl_place.objects.all()
    if request.method=="POST":
        place=request.POST.get("txt_place")
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=place,district=district)
        return render(request,'Admin/Place.html',{'msg':'data inserted'})  
    else:
        return render(request,"Admin/Place.html",{'district':ddata,'place':pdata}) 
def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")
def editplace(request,id):
    d=tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=id)
    if request.method=="POST":
        place=request.POST.get("txt_place")
        editdata.district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        editdata.place_name=place
        editdata.save()
        return redirect("Admin:place")
    else:    
       return render(request,'Admin/Place.html',{'editdata':editdata,'district':d}) 
def subcategory(request):
    cdata=tbl_category.objects.all()
    sdata=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcategory=request.POST.get("txt_subcategory")
        category=tbl_category.objects.get(id=request.POST.get("sel_category"))
        tbl_subcategory.objects.create(subcategory_name=subcategory,category=category)
        return render(request,"Admin/Subcategory.html",{'msg':'data inserted'})
    else:
        return render(request,"Admin/Subcategory.html",{'category':cdata,'subcategory':sdata})  
def delsubcategory(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:subcategory") 
def editsubcategory(request,id):
    c=tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
        subcategory=request.POST.get("txt_subcategory")
        editdata.category=tbl_category.objects.get(id=request.POST.get("sel_category"))
        editdata.subcategory_name=subcategory
        editdata.save()
        return redirect("Admin:subcategory")
    else:    
       return render(request,'Admin/Subcategory.html',{'editdata':editdata,'category':c})          
def userlist(request):
    if "aid" not in request.sesion:
        return redirect("Guest/Login.html")
    else:
        userdata=tbl_user.objects.all()
        return render(request,'Admin/UserList.html',{"users":userdata})
def sclist(request):
    if "aid" not in request.sesion:
        return redirect("Guest/Login.html")
    else:
        scdata=tbl_servicecentre.objects.all()
        return render(request,'Admin/SCList.html',{"sc":scdata})
def scverification(request):
    if "aid" not in request.sesion:
        return redirect("Guest/Login.html")
    else:
        pending=tbl_servicecentre.objects.filter(servicecentre_status=0)
        accepted=tbl_servicecentre.objects.filter(servicecentre_status=1)
        rejected=tbl_servicecentre.objects.filter(servicecentre_status=2)
        return render(request,'Admin/SCVerification.html',{"pending":pending,'accepted':accepted,'rejected':rejected})
def scaccept(request,aid):
     scdata=tbl_servicecentre.objects.get(id=aid)
     scdata.servicecentre_status = 1
     scdata.save()
     return render(request,'Admin/SCVerification.html',{'msg':"Verified.."})
def screject(request,rid):
     scdata=tbl_servicecentre.objects.get(id=rid)
     scdata.servicecentre_status = 2
     scdata.save()
     return render(request,'Admin/SCVerification.html',{'msg':"Rejected.."})
def viewrequest(request):
    if "aid" not in request.sesion:
        return redirect("Guest/Login.html")
    else:
        data=tbl_request.objects.all()
        return render(request,'Admin/ViewRequest.html',{"sc":data})
def accept(request,aid):
     data=tbl_request.objects.get(id=aid)
     data.request_status = 1
     data.request_starttime=datetime.now()
     data.save()
     return render(request,'Admin/ViewRequest.html',{'msg':"Accepted.."})
def reject(request,rid):
     data=tbl_request.objects.get(id=rid)
     data.servicecentre_status = 2
     data.save()
     return render(request,'Admin/ViewRequest.html',{'msg':"Rejected.."})

def viewsc(request,rid):
    data=tbl_servicecentre.objects.filter(servicecentre_status=1)
    return render(request,'Admin/ViewSC.html',{"sc":data,'rid':rid})

def assign(request,rid,sid):
    reqdata=tbl_request.objects.get(id=rid)
    reqdata.servicecentre = tbl_servicecentre.objects.get(id=sid)
    reqdata.request_status=3
    reqdata.save()
    return render(request,'Admin/ViewRequest.html',{'msg':"Assigned.."})