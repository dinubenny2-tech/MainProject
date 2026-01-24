from django.shortcuts import render, redirect
from Guest.models import *
from ServiceCentre.models import *
from Worker.models import *
from User.models import *
from datetime import timedelta, datetime,date
from django.utils import timezone
from django.core.files.base import ContentFile
from xhtml2pdf import pisa
from io import BytesIO
import base64

LIMIT = timedelta(days=6)

def calculate_progress(obj):
    obj.remaining_text = "Not Started"
    if not obj.request_starttime:
        return
    start = obj.request_starttime
    end = obj.request_endtime
    now = timezone.now()
    if end:
        obj.remaining_text = "✓ Completed"
        return
    deadline = start + LIMIT
    remaining = deadline - now
    if remaining.total_seconds() <= 0:
        obj.remaining_text = "Overdue"
        return
    days = remaining.days
    hours = remaining.seconds // 3600
    obj.remaining_text = f"{days}d {hours}h left" if days > 0 else f"{hours}h left"

def HomePage(request):
    if "wid" not in request.session:
        return redirect("Guest/Login.html")
    return render(request,'Worker/HomePage.html')

def myprofile(request):
    if "wid" not in request.session:
        return redirect("Guest/Login.html")
    wdata = tbl_worker.objects.get(id=request.session["wid"])
    return render(request,'Worker/MyProfile.html',{"wdata":wdata})

def editprofile(request):
    wdata = tbl_worker.objects.get(id=request.session["wid"])
    if request.method=="POST":
        wdata.worker_name = request.POST.get('txt_name')
        wdata.worker_email = request.POST.get('txt_email')
        wdata.worker_contact = request.POST.get('txt_contact')
        wdata.worker_address = request.POST.get('txt_address')
        wdata.save()
        return render(request,'Worker/EditProfile.html',{'msg':"updated"})
    return render(request,'Worker/EditProfile.html',{"wdata":wdata})

def changepassword(request):
    wdata = tbl_worker.objects.get(id=request.session['wid'])
    if request.method=="POST":
        oldpass = request.POST.get('txt_oldpass')
        newpass = request.POST.get('txt_newpass')
        repass = request.POST.get('txt_repass')
        if wdata.worker_password == oldpass:
            if newpass == repass:
                wdata.worker_password = newpass
                wdata.save()
                return render(request,'Worker/ChangePassword.html',{'msg':"Password Updated.."})
            return render(request,"Worker/ChangePassword.html",{'msg1':"Password Mismatch.."})
        return render(request,'Worker/ChangePassword.html',{'msg1':"Password Incorrect.."})
    return render(request,'Worker/ChangePassword.html')

def viewwork(request):
    if "wid" not in request.session:
        return redirect("Guest/Login.html")
    workerdata = tbl_worker.objects.get(id=request.session['wid'])
    data = tbl_request.objects.filter(request_status=3, servicecentre=workerdata.servicecentre_id)
    return render(request,'Worker/ViewWork.html',{"work":data})

def join(request, aid):
    data = tbl_request.objects.get(id=aid)
    data.request_status = 4
    data.worker = tbl_worker.objects.get(id=request.session['wid'])
    data.save()
    return redirect('Worker:myworks')

def myworks(request):
    worker_id = request.session.get('wid')
    if not worker_id:
        return redirect('Guest/Login.html')

    data = tbl_request.objects.filter(worker_id=worker_id, request_status__gte=4)

    replacement = tbl_request.objects.filter(
        worker_id=worker_id,
        request_status__gte=4,
        request_status__lte=7
    )

    repair = tbl_request.objects.filter(
        worker_id=worker_id,
        request_status__gte=9,
        request_status__lte=13
    )

    for qs in [data, replacement, repair]:
        for i in qs:
            calculate_progress(i)

    return render(request, "Worker/MyWorks.html", {
        "data": data,
        "replacement": replacement,
        "repair": repair
    })

def replacement(request, rid):
    data = tbl_request.objects.get(id=rid)
    data.request_status = 5
    data.save()
    return redirect('Worker:myworks')

def repair(request, aid):
    data = tbl_request.objects.get(id=aid)
    data.request_status = 8
    data.save()
    return redirect('Worker:todate', id=aid)

def viewfile(request,id):
    data = tbl_request.objects.get(id=id)
    return render(request,'Worker/ViewFile.html',{"work":data})

def todate(request, id):
    data = tbl_request.objects.get(id=id)
    today = date.today()
    if request.method == "POST":
        todate = request.POST.get('txt_date')
        data.request_todate = todate
        data.request_status = 10
        data.save()
        return render(request, 'Worker/Todate.html', {'msg': "Date Uploaded..", 'today': today})
    else:
        return render(request, 'Worker/Todate.html', {'today': today})

def assessment(request):
    return render(request,'Worker/Assessment.html')

def form(request, id):
    data = tbl_request.objects.get(id=id)
    if request.method == "POST":
        code = request.POST.get("txt_code")
        sino = request.POST.get("txt_sino")
        qty = request.POST.get("txt_qty")
        vol = request.POST.get("txt_vol")
        amp = request.POST.get("txt_amp")
        app = request.POST.get("txt_app")
        period = request.POST.get("txt_period")
        complaint = request.POST.get("txt_complaint")
        action = request.POST.get("txt_action")
        signature = request.POST.get("signature_data")
        format, imgstr = signature.split(';base64,')
        ext = format.split('/')[-1]
        sign_file = ContentFile(base64.b64decode(imgstr), name='sign.' + ext)
        rep = tbl_replacement.objects.create(
            replacement_code=code,
            replacement_sino=sino,
            replacement_qty=qty,
            replacement_voltage=vol,
            replacement_ampere=amp,
            replacement_app=app,
            replacement_period=period,
            replacement_complaint=complaint,
            replacement_status=action,
            replacement_signature=sign_file,
            request=data
        )
        data.request_status = 7
        data.request_endtime = datetime.now()
        data.save()
        sig_data_uri = f"data:image/{ext};base64,{imgstr}"
        html = render(request, "Worker/FormPDF.html", {"data": data, "rep": rep, "today": datetime.today().date(), "signature_base64": sig_data_uri}).content.decode("utf-8")
        pdf_buffer = BytesIO()
        pisa.CreatePDF(html, dest=pdf_buffer)
        rep.replacement_pdf.save(f"work_{rep.id}.pdf", ContentFile(pdf_buffer.getvalue()), save=True)
        return redirect(rep.replacement_pdf.url)
    return render(request, "Worker/Form.html", {"data": data, "today": datetime.today().date()})


def risk_assessment(request, id):
    work = tbl_request.objects.get(id=id)
    if request.method == "POST":
        risk_items = request.POST.getlist("risk")  # checkbox values

        if len(risk_items) < 12:  # all must be checked
            work.request_status = 11  # cancelled
            work.save()
            msg = "Risk Assessment Failed. Work Cancelled."
            return render(request, "Worker/RiskAssessment.html", {"work": work, "msg": msg})
        else:
            work.request_status = 12  # approved, can start work
            work.save()
            return redirect("Worker:myworks")
    return render(request, "Worker/RiskAssessment.html", {"work": work})


def start_work(request, id):
    work = tbl_request.objects.get(id=id)
    work.request_status = 12
    work.request_starttime = timezone.now()
    work.save()
    return redirect("Worker:myworks")


def end_work(request, id):
    work = tbl_request.objects.get(id=id)
    work.request_status = 13
    work.request_endtime = timezone.now()
    work.save()
    return redirect("Worker:myworks")


def complete_work(request, id):
    data = tbl_request.objects.get(id=id)

    if request.method == "POST":
        amount = request.POST.get('txt_amount')
        data.request_amount = amount
        data.request_endtime = datetime.now()
        data.request_status = 13  # Completed
        data.save()
        return render(request, "Worker/CompleteWork.html", {
            "data": data,
            "msg": "Work Completed Successfully!"
        })

    return render(request, "Worker/CompleteWork.html", {"data": data})
