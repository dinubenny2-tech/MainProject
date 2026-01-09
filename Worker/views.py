from django.shortcuts import render
from Guest.models import*
from ServiceCentre.models import*
from Worker.models import*
from User.models import*

def HomePage(request):
    return render(request,'Worker/HomePage.html')
def myprofile(request):
    wdata=tbl_worker.objects.get(id=request.session["wid"])
    return render(request,'Worker/MyProfile.html',{"wdata":wdata})
def editprofile(request):
    wdata=tbl_worker.objects.get(id=request.session["wid"])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        wdata.worker_name=name
        wdata.worker_email=email
        wdata.worker_contact=contact
        wdata.worker_address=address
        wdata.save()
        return render(request,'Worker/EditProfile.html',{'msg':"updated"})
    else:
        return render(request,'Worker/EditProfile.html',{"wdata":wdata})
def changepassword(request):
    wdata=tbl_worker.objects.get(id=request.session['wid'])
    wpassword = wdata.worker_password
    if request.method=="POST":
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        repass=request.POST.get('txt_repass')
        if wpassword == oldpass:
            if newpass == repass:
                wdata.worker_password = newpass
                wdata.save()
                return render(request,'Worker/ChangePassword.html',{'msg':"Password Updated.."})
            else:
                return render(request,"Worker/ChangePassword.html",{'msg1':"Password Mismatch.."})
        else:
            return render(request,'Worker/ChangePassword.html',{'msg1':"Password Incorrect.."})
    else:
        return render(request,'Worker/ChangePassword.html')
def viewwork(request):
    data=tbl_request.objects.filter(request_status=3)
    return render(request,'Worker/ViewWork.html',{"work":data})
def join(request,aid):
     data=tbl_request.objects.get(id=aid)
     data.request_status = 4
     data.worker=tbl_worker.objects.get(id=request.session['wid'])
     data.save()
     return render(request,'Worker/ViewWork.html',{'msg':"Work Accepted.."})
def myworks(request):
    data=tbl_request.objects.filter(request_status=4) 
    replacement=tbl_request.objects.filter(request_status__gte=5,request_status__lte=8)
    repair=tbl_request.objects.filter(request_status__gte=9)
    return render(request,'Worker/MyWorks.html',{'data':data,'replacement':replacement,'repair':repair})
def replacement(request,rid):
     data=tbl_request.objects.get(id=rid)
     data.request_status = 6
     data.save()
     return render(request,'Worker/MyWorks.html',{'msg':"Product need Replacement.."})
def repair(request,aid):
     data=tbl_request.objects.get(id=aid)
     data.request_status = 9
     data.save()
     return render(request,'Worker/MyWorks.html',{'msg':"Product need Repair.."})
def viewfile(request,id):
   
    data=tbl_request.objects.filter(id=id,request_status=7)
    return render(request,'Worker/ViewFile.html',{"work":data})
def todate(request,id):
    data=tbl_request.objects.get(id=id)
    if request.method=="POST":
        todate=request.POST.get('txt_date')
        data.request_todate = todate
        data.request_status = 10
        data.save()
        return render(request,'Worker/Todate.html',{'msg':"Date Uploaded.."})
    else:
        return render(request,'Worker/Todate.html')
# Create your views here.
