from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path , include
from . import views , settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.show_home),
    path('' , include('login_page.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


