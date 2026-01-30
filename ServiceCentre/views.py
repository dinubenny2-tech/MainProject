from django.shortcuts import render,redirect
from Guest.models import*
from ServiceCentre.models import*
from User.models import*

def HomePage(request):
    if "scid" not in request.session:
        return redirect("Guest/Login.html")
    else:
        return render(request,'ServiceCentre/HomePage.html')
def myprofile(request):
    if "scid" not in request.session:
        return redirect("Guest/Login.html")
    else:
        scdata=tbl_servicecentre.objects.get(id=request.session["scid"])
        return render(request,'ServiceCentre/MyProfile.html',{"scdata":scdata})
def editprofile(request):
    scdata=tbl_servicecentre.objects.get(id=request.session["scid"])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        scdata.servicecentre_name=name
        scdata.servicecentre_email=email
        scdata.servicecentre_contact=contact
        scdata.servicecentre_address=address
        scdata.save()
        return render(request,'ServiceCentre/EditProfile.html',{'msg':"updated"})
    else:
        return render(request,'ServiceCentre/EditProfile.html',{"scdata":scdata})
def changepassword(request):
    scdata=tbl_servicecentre.objects.get(id=request.session['scid'])
    scpassword = scdata.servicecentre_password
    if request.method=="POST":
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        repass=request.POST.get('txt_repass')
        if scpassword == oldpass:
            if newpass == repass:
                scdata.servicecentre_password = newpass
                scdata.save()
                return render(request,'ServiceCentre/ChangePassword.html',{'msg':"Password Updated.."})
            else:
                return render(request,"ServiceCentre/ChangePassword.html",{'msg1':"Password Mismatch.."})
        else:
            return render(request,'ServiceCentre/ChangePassword.html',{'msg1':"Password Incorrect.."})
    else:
        return render(request,'ServiceCentre/ChangePassword.html')
def wregistration(request):
    if "scid" not in request.session:
        return redirect("Guest/Login.html")
    else:
        servicecentre=tbl_servicecentre.objects.get(id=request.session["scid"])
        district=tbl_district.objects.all()
        place=tbl_place.objects.all()
        wdata=tbl_worker.objects.all()

        if request.method=="POST":
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            contact=request.POST.get("txt_contact")
            address=request.POST.get("txt_address")
            photo=request.FILES.get("file_photo")
            password=request.POST.get("txt_password")
            place=tbl_place.objects.get(id=request.POST.get("sel_place"))
            checkwemail = tbl_worker.objects.filter(worker_email=email).count()
            if checkwemail > 0:
                return render(request,"ServiceCentre/WorkerRegistration.html",{'msg':"Email Already Exist"})
            else:
                tbl_worker.objects.create(worker_name=name,worker_email=email,worker_contact=contact,worker_address=address,worker_photo=photo,worker_password=password,place=place,servicecentre_id=servicecentre)
            return render(request,'ServiceCentre/WorkerRegistration.html',{'msg':"registered"})
        else:
            return render(request,'ServiceCentre/WorkerRegistration.html',{'district':district,'place':place,'wdata':wdata})
def viewrequest(request):
    if "scid" not in request.session:
        return redirect("Guest/Login.html")
    else:
        data=tbl_request.objects.filter(servicecentre=request.session['scid'])
        return render(request,'ServiceCentre/ViewRequest.html',{"sc":data})
    

def reassign_worker(request, id):
    if "scid" not in request.session:
        return redirect("Guest:login")
    workers = tbl_worker.objects.filter(servicecentre_id=request.session['scid'])
    if request.method == "POST":
        wid = request.POST.get("wid")

        tbl_request.objects.filter(id=id).update(
            worker_id=wid,   
            request_status=4
        )
        return redirect("ServiceCentre:viewrequest")
    else:
        return render(request, 'ServiceCentre/ViewWorker.html', {"worker": workers})
    

