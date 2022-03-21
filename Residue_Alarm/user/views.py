from . import serializers
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.
from rest_framework.settings import api_settings
class CreateUserView(generics.CreateAPIView):
    '''Crear nuevo usuario en el proyecto'''
    serializer_class = serializers.UserSerializer

class CreateTokenView(ObtainAuthToken):
    '''Crear Nuevo token para usuario'''
    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES