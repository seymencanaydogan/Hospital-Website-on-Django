from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('hakkimizda', views.hakkimizda , name='hakkimizda'),
    path('sss', views.faq , name='faq'),
    path('iletisim', views.iletisim , name='iletisim'),
    path('tibbi-birimler', views.kategori , name='kategori'),
    path('Policlinic/', include('Policlinic.urls')),
    path('', include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('tibbi-birimler/<int:id>/<slug:slug>', views.kategori_policlinics , name='kategori_policlinics'),
    path('policlinic/<int:id>/<slug:slug>', views.policlinic_details , name='policlinic_details'),
    path('policlinic/addcomment/<int:id>',views.addcomment,name='addcomment'),
    path('search/',views.policlinic_search,name='policlinic_search'),
    path('doktorlar',views.doctors,name='doctors'),
    path('logout/',views.logout_view,name='logout_view'),
    path('login/',views.login_view,name='login_view'),
    path('register/',views.register_view,name='register_view'),
    path('randevu',views.randevu,name='randevu'),
    path('profile',views.profile,name='profile'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
