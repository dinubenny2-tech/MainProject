from django.shortcuts import render,redirect
from Guest.models import*
from User.models import *
from Worker.models import*
from datetime import datetime
from django.db.models import Q
from django.http import JsonResponse
def myprofile(request):
    if "uid" not in request.session:
        return redirect("Guest/Login.html")
    else:
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
    if "uid" not in request.session:
        return redirect("Guest/Login.html")
    else:
        return render(request,'User/HomePage.html')
def complaint(request):
    if "uid" not in request.session:
        return redirect("Guest/Login.html")
    else:
        userdata=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            title=request.POST.get('txt_title')
            content=request.POST.get('txt_des')
            tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=userdata)
            return render(request,'User/Complaint.html',{'msg':"Complaint submitted.."})
        else:
            return render(request,'User/Complaint.html')

def viewsc(request):
    if "uid" not in request.session:
        return redirect("Guest/Login.html")
    else:
        scdata=tbl_servicecentre.objects.filter(servicecentre_status=1)
        return render(request,'User/ViewSC.html',{"sc":scdata})
def screquest(request,rid):
     screquest=tbl_request.objects.get(id=rid)
     return render(request,'User/Request.html',{'msg':"Requested.."})
def request(request):
    if "uid" not in request.session:
        return redirect("Guest/Login.html")
    else:
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
    if "uid" not in request.session:
        return redirect("Guest/Login.html")
    else:
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
        photo=request.FILES.get('file_photo')
        bill=request.FILES.get('file_bill')
        rdata.product_photo=photo
        rdata.product_bill=bill
        rdata.request_status=6
        rdata.save()
        return render(request,'User/Upload.html',{'msg':"Uploaded.."})
    else:
        return render(request,'User/Upload.html')
def viewform(request,id):
    data=tbl_request.objects.get(id=id)
    rdata=tbl_replacement.objects.get(request=data)
    return render(request,'User/ViewForm.html',{'data':data,'rdata':rdata})
def chatpage(request,id):
    worker = tbl_worker.objects.get(id=id)
    return render(request,"User/Chat.html",{"worker":worker})
def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_worker = tbl_worker.objects.get(id=request.POST.get("tid"))
    print(to_worker)
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,worker_to=to_worker,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")
def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(worker_from=tid) | Q(worker_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})
def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(worker_to=request.GET.get("tid")) | (Q(worker_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})
def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(servicecentre=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(servicecentre=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session['uid']),user_review=user_review,rating_data=rating_data,servicecentre=tbl_servicecentre.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(servicecentre=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(servicecentre=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(servicecentre=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)







# Create your views here.
