from django.contrib import admin
from home.models import Setting,ContactFormMessage,UserProfile,FAQ

class SettingAdmin(admin.ModelAdmin):
    list_display=['title','status']
    list_filter=['status']

class ContactFormAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message','note','status']
    list_filter=['status']

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','email','phone','city','country','image_tag','status']
    list_filter=['status']

class FAQAdmin(admin.ModelAdmin):
    list_display=['question','answer','status']
    list_filter=['status']

admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactFormMessage,ContactFormAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(FAQ,FAQAdmin)