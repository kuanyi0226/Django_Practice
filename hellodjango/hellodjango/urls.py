from django.contrib import admin
from django.conf.urls import url, include

from music.views import hello_view

urlpatterns = [
    url('admin/', admin.site.urls),
    url('hello/', hello_view), #建立路由
]
