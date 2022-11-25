from django.contrib import admin

# Register your models here.
#註冊model: 可以在網頁後台管理資料
from music.models import Music

admin.site.register(Music)