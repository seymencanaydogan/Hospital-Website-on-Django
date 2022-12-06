from django.contrib import admin
from Policlinic.models import Category , Policlinic , Images

class PoliclinicImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class PoliclinicAdmin(admin.ModelAdmin):
    list_display = ['title','category','image','status']
    list_filter = ['status']
    inlines = [PoliclinicImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','policlinic','image']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Policlinic,PoliclinicAdmin)
admin.site.register(Images,ImagesAdmin)