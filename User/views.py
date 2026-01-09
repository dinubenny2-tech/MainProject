from django.shortcuts import render
from Guest.models import*
from User.models import *

def myprofile(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    return render(request,'User/MyProfile.html',{"userdata":userdata})
def editprofile(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        userdata.user_name=name
        userdata.user_email=email
        userdata.user_contact=contact
        userdata.user_address=address
        userdata.save()
        return render(request,'User/EditProfile.html',{'msg':"updated"})
    else:
        return render(request,'User/EditProfile.html',{"userdata":userdata})
def changepassword(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    userpassword = userdata.user_password
    if request.method=="POST":
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        repass=request.POST.get('txt_repass')
        if userpassword == oldpass:
            if newpass == repass:
                userdata.user_password = newpass
                userdata.save()
                return render(request,'User/ChangePassword.html',{'msg':"Password Updated.."})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Password Mismatch.."})
        else:
            return render(request,'User/ChangePassword.html',{'msg1':"Password Incorrect.."})
    else:
        return render(request,'User/ChangePassword.html')
def HomePage(request):
    return render(request,'User/HomePage.html')
def complaint(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        title=request.POST.get('txt_title')
        content=request.POST.get('txt_des')
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=userdata)
        return render(request,'User/Complaint.html',{'msg':"Complaint submitted.."})
    else:
         return render(request,'User/Complaint.html')

def viewsc(request):
    scdata=tbl_servicecentre.objects.filter(servicecentre_status=1)
    return render(request,'User/ViewSC.html',{"sc":scdata})
def screquest(request,rid):
     screquest=tbl_request.objects.get(id=rid)
     return render(request,'User/Request.html',{'msg':"Requested.."})
def request(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        emergency=request.POST.get('txt_emergency')
        reason = request.POST.get("txt_reason")
        details=request.POST.get('txt_details')
        tbl_request.objects.create(request_emergency=emergency,request_details=details,user=userdata,request_emdetails=reason)
        return render(request,'User/Request.html',{'msg':"Request submitted.."})
    else:
        return render(request,'User/Request.html')
def myrequest(request):
    data=tbl_request.objects.filter(user=request.session['uid'])
    return render(request,'User/MyRequest.html',{"sc":data})
def assign(request,aid):
     data=tbl_request.objects.get(id=aid)
     data.servicecentre_status = 3
     data.save()
     return render(request,'Admin/ViewSC.html',{'msg':"Assigned.."})
def upload(request,id):
    data=tbl_request.objects.filter(user=request.session['uid'])
    rdata=tbl_request.objects.get(id=id)
    if request.method=="POST":
        photo=request.POST.get('file_photo')
        bill=request.POST.get('file_bill')
        rdata.product_photo=photo
        rdata.product_bill=bill
        rdata.request_status=6
        rdata.save()
        return render(request,'User/Upload.html',{'msg':"Uploaded.."})
    else:
        return render(request,'User/Upload.html')
# Create your views here.
