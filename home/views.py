from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting

def index(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting, 'page':'home'}
    return render(request,'index.html',context)

def hakkimizda(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting , 'page':'hakkimizda'}
    return render(request,'hakkimizda.html',context)

def referans(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting , 'page':'referans'}
    return render(request,'referans.html',context)

def iletisim(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting , 'page':'iletisim'}
    return render(request,'iletisim.html',context)