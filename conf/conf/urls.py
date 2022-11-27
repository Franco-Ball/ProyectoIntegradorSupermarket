"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from confApp.views import(
    home_screen_view,
    signin_screen_view,
    cajeros_view,
    cambio_DB,
    art_update,
    home_screen_view2,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('signin/', signin_screen_view, name='signin'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("cajeros/base/", cajeros_view, name="base"),
    path("changeDB/", cambio_DB, name="changeDB"),
    path("updateArt/<articulo_id>", art_update, name="update-art"),
    path('listArt/',home_screen_view2 , name='listado'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)