# Create your views here.
from music.models import Music
from music.serializers import MusicSerializer

from rest_framework import viewsets #比原本的views好
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet): #有CRUD的特性
    queryset = Music.objects.all() #覆寫
    serializer_class = MusicSerializer #覆寫
    permission_classes = (IsAuthenticated,)