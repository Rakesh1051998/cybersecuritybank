from itertools import count

from django.db.models import Count
from django.shortcuts import render, redirect


# Create your views here.
from admins.models import Sendquery
from cyber_alert.models import GiverTransaction, AdminRegister


def admin_page(request):
    if request.method == "POST":
        admin = request.POST.get('admin')
        password = request.POST.get('password')
        if admin == "admin" and password == "admin":
            return redirect('analyze')

    return render(request,'admins/admin_page.html')

def analyze(request):
    topic = GiverTransaction.objects.values('date', 'name').annotate(dcount=Count('month')).order_by('-dcount')

    return render(request, "admins/analyze.html", {'form':topic})


def adlogout(request):
    return redirect('admin_page')

def charts(request,chart_type):
    chart = GiverTransaction.objects.values('month').annotate(dcount=Count('month'))

    return render(request,"admins/charts.html", {'form':chart, 'chart_type':chart_type})

def riskuser(request):
    obj = GiverTransaction.objects.filter(amount__range=(500000, 2500000))

    return render(request, 'admins/riskuser.html', {'objv': obj})

def riskalert(request,tuser):

    obj = GiverTransaction.objects.get(id=tuser)

    if request.method == "POST":
        admin = request.POST.get('name')
        names = request.POST.get('name1')
        Sendquery.objects.create(transid=obj,sendquery=admin, name=names)




    return render(request, 'admins/riskalert.html')

