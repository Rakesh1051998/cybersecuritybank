from itertools import count

from MySQLdb import Date
from django.contrib import messages
from django.db.models import Count

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from admins.models import Sendquery
from cyber_alert import forms
from cyber_alert.forms import AdminForm, GiverForm
from cyber_alert.models import GiverTransaction, AdminRegister


def admin_login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            check = AdminRegister.objects.get(name=name, password=password)
            request.session['name'] = check.id

            return redirect('giver_transaction')
        except:
            pass


    return render(request, "admin_login.html")

def admin_register(request):
    if request.method == "POST":
        forms = AdminForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'You have been successfully registered')
            return redirect('admin_login')
    else:
        forms = AdminForm()


    return render(request,'admin_register.html',{'form':forms})

def giver_transaction(request):
    sd=''
    aas=''
    sw=''
    q=''
    name = request.session['name']
    obj = AdminRegister.objects.get(id=name)
    if request.method == "POST":
        name = request.POST.get('name')
        aadhar = request.POST.get('aadharno')
        address = request.POST.get('address')
        mobile = request.POST.get('mobileno')
        bank = request.POST.get('bankname')
        account= request.POST.get('accountno')
        branch=request.POST.get('branchname')
        amount=request.POST.get('amount')
        ifsc= request.POST.get('ifsccode')
        micr=request.POST.get('micrcode')
        date=request.POST.get('date')
        time= request.POST.get('time')
        transaction=request.POST.get('transactionid')
        sd=date.split("-")
        GiverTransaction.objects.create(userid=obj,day=sd[0],month=sd[1],year=sd[2],name=name,aadharno=aadhar,address=address,mobileno=mobile,bankname=bank,accountno=account,branchname=branch,amount=amount,ifsccode=ifsc,micrcode=micr,date=date,time=time,transationid=transaction)




    return render(request,'giver_transaction.html',{'form':sd,'we':q})



def analyze_page(request):
    name = request.session['name']
    admin_obj = AdminRegister.objects.get(id=name)
    to_name = admin_obj.name
    obj = GiverTransaction.objects.filter(name=to_name, )

    return render(request, 'analyze_page.html', {'objv': obj})

def viewer(request,chart_type):
    chart = GiverTransaction.objects.values('month').annotate(dcount=Count('month'))

    return render(request,"viewer.html",{'form':chart,'chart_type':chart_type})

def update(request):
    name = request.session['name']
    obj = AdminRegister.objects.get(id=name)
    if request.method == "POST":
        Admin_Id = request.POST.get('adminid', '')
        Name  = request.POST.get('name', '')
        Email = request.POST.get('email', '')
        Password = request.POST.get('password', '')
        Phone_Number = request.POST.get('phoneno', '')
        Address = request.POST.get('address', '')

        obj = get_object_or_404(AdminRegister, id=name)
        obj.adminid = Admin_Id
        obj.name = Name
        obj.email = Email
        obj.password = Password
        obj.phoneno = Phone_Number
        obj.address = Address
        obj.save(update_fields=["adminid", "name", "email", "password", "phoneno", "address" ])
        return redirect('admin_login')
    return render(request, 'update.html',{'objc':obj})

def logout_page(request):
    return redirect(admin_login)

def mydetails(request):
    name = request.session["name"]
    obj= AdminRegister.objects.get(id=name)
    if request.method == "POST":
        Admin_Id = request.POST.get('adminid','')
        Name = request.POST.get('name', '')
        Email = request.POST.get('email', '')
        Password = request.POST.get('password', '')
        Phone_Number = request.POST.get('phoneno', '')
        Address = request.POST.get('address', '')

        obj= get_object_or_404(AdminRegister, id=name)
        obj.adminid = Admin_Id
        obj.name = Name
        obj.email = Email
        obj.password = Password
        obj.phoneno = Phone_Number
        obj.address = Address

    return render(request, 'mydetails.html', {'objc': obj})

def show(request):
    return render(request,'show.html' )
def receivealert(request):
    name = request.session['name']
    admin_obj = AdminRegister.objects.get(id=name)
    to_name = admin_obj.name
    obj=Sendquery.objects.filter(name=to_name)

    return render(request, 'receivealert.html',{'de':obj})