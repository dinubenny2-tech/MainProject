from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
from ServiceCentre.models import*
from Worker.models import*

def index(request):
    return render(request,'Guest/index.html')

def userregistration(request):
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if  request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        password=request.POST.get("txt_password")
        photo=request.FILES.get("file_photo")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        checkuseremail = tbl_user.objects.filter(user_email=email).count()
        if checkuseremail > 0:
            return render(request,"Guest/UserRegistration.html",{'msg':"Email Already Exist"})
        else:

            tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_password=password,
            user_photo=photo,place=place,)
            return render(request,'Guest/UserRegistration.html',{'msg':"registered"})
    else:
        return render(request,'Guest/UserRegistration.html',{'district':district,'place':place})


def ajaxplace(request):
    district=tbl_district.objects.get(id=request.GET.get("did"))
    place=tbl_place.objects.filter(district=district)
    return render(request,"Guest/AjaxPlace.html",{"place":place}) 

def login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")

        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount = tbl_user.objects.filter(user_email=email,user_password=password).count()
        sccount=tbl_servicecentre.objects.filter(servicecentre_email=email,servicecentre_password=password).count()
        wcount=tbl_worker.objects.filter(worker_email=email,worker_password=password).count()
        if admincount > 0:
            admindata = tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["aid"] = admindata.id
            return redirect("Admin:HomePage")
        elif usercount > 0:
            userdata = tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"] = userdata.id
            return redirect("User:HomePage")
        elif sccount > 0:
            scdata = tbl_servicecentre.objects.get(servicecentre_email=email,servicecentre_password=password)
            request.session["scid"] = scdata.id
            return redirect("ServiceCentre:HomePage")
        elif wcount > 0:
            wdata = tbl_worker.objects.get(worker_email=email,worker_password=password)
            request.session["wid"] = wdata.id
            return redirect("Worker:HomePage")
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Email Or Password.."})
    else:
        return render(request,'Guest/Login.html')
def scregistration(request):
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        details=request.POST.get("txt_details")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("file_photo")
        proof=request.FILES.get("file_proof")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        checkscemail = tbl_servicecentre.objects.filter(servicecentre_email=email).count()
        if checkscemail > 0:
            return render(request,"Guest/ServiceCentre.html",{'msg':"Email Already Exist"})
        else:
            tbl_servicecentre.objects.create(servicecentre_name=name,servicecentre_details=details,servicecentre_address=address,servicecentre_photo=photo,servicecentre_proof=proof,servicecentre_contact=contact,servicecentre_email=email,servicecentre_password=password,place=place,)
            return render(request,'Guest/ServiceCentre.html',{'msg':"registered"})
    else:
        return render(request,'Guest/ServiceCentre.html',{'district':district,'place':place})


# Create your views here.
