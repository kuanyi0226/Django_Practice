from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from music.views import MusicViewSet

router = DefaultRouter()
router.register('music', MusicViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # for rest_framework
    path('api/', include(router.urls)),
    # for rest_framework auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]