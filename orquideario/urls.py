
from django.contrib import admin
from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^servicios_orquideario/', include('servicios_orquideario.urls')),
]
