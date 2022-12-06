from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting

def index(request):
    setting=Setting.objects.get(id=1)
    context={'setting':setting}
    return render(request,'index.html',context)