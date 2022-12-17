from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('hakkimizda', views.hakkimizda , name='hakkimizda'),
    path('referans', views.referans , name='referans'),
    path('iletisim', views.iletisim , name='iletisim'),
    path('tibbi-birimler', views.kategori , name='kategori'),
    path('Policlinic/', include('Policlinic.urls')),
    path('', include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
