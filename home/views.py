from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from home.models import Setting, ContactFormu, ContactFormMessage
from Policlinic.models import Policlinic,Category,Images

def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Policlinic.objects.all().order_by('?')[:4]
    category=Category.objects.all()
    policlinicdata=Policlinic.objects.all().order_by('?')[:3]
    context={'page':'home','setting':setting, 'category':category, 'sliderdata':sliderdata, 'policlinicdata':policlinicdata}
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

def kategori(request):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    context={'setting':setting ,'category':category,'page':'kategori'}
    return render(request,'kategori.html',context)

def kategori_policlinics(request,id,slug):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    policlinics=Policlinic.objects.filter(category_id=id)
    context={'setting':setting ,'policlinics':policlinics, 'category':category, 'slug':slug}
    return render(request,'klinikler.html',context)

def policlinic_details(request,id,slug):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    images=Images.objects.filter(policlinic_id=id)
    policlinic=Policlinic.objects.filter(pk=id)
    context={'setting':setting ,'policlinic':policlinic, 'category':category, 'images':images, 'slug':slug}
    return render(request,'policlinic_details.html',context)