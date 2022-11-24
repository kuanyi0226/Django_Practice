from django.db import models


# Create your models here.
#4個欄位的SQLite資料庫
class Music(models.Model):
    #id欄位會自動產生
    song = models.TextField(default="song")
    singer = models.TextField(default="AKB48")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"
