from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from home.models import Setting, ContactFormu, ContactFormMessage

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
    if request.method=='POST':
        form=ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız başarıyla iletildi. Teşekkürler!")
            return HttpResponseRedirect('iletisim')
    
    setting=Setting.objects.get(pk=1)
    form=ContactFormu()
    context={'setting':setting , 'form':form}
    return render(request,'iletisim.html',context)