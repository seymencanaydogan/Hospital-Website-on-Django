from django.contrib import admin
from home.models import Setting,ContactFormMessage

class SettingAdmin(admin.ModelAdmin):
    list_display=['title','status']
    list_filter=['status']

class ContactFormAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message','note','status']
    list_filter=['status']

admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactFormMessage,ContactFormAdmin)
