from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import main.views as main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("", main.registrarDatos),
    path("newUser/", main.registrarDatos),
    path("signIn/", main.signIn),
    path("search/", main.search),
    path("modifyUser/", main.modify)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
