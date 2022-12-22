from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from Policlinic.models import Category , Policlinic , Images, Comment

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

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','policlinic','user','status']
    list_filter = ['status']

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','policlinic','image']

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_policlinics_count', 'related_policlinics_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Policlinic,
                'category',
                'policlinics_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Policlinic,
                 'category',
                 'policlinics_count',
                 cumulative=False)
        return qs

    def related_policlinics_count(self, instance):
        return instance.policlinics_count
    related_policlinics_count.short_description = 'Related policlinics (for this specific category)'

    def related_policlinics_cumulative_count(self, instance):
        return instance.policlinics_cumulative_count
    related_policlinics_cumulative_count.short_description = 'Related policlinics (in tree)'

admin.site.register(Category,CategoryAdmin2)
admin.site.register(Policlinic,PoliclinicAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)