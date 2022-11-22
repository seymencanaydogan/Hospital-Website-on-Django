from django.contrib import admin
from Policlinic.models import Category , Policlinic

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class PoliclinicAdmin(admin.ModelAdmin):
    list_display = ['title','category','status']
    list_filter = ['status']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Policlinic,PoliclinicAdmin)