from . import serializers
from rest_framework import generics, authentication , permissions
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

class ManageUserView(generics.RetrieveUpdateAPIView):
    '''Maneja al usuario autenticado'''
    serializer_class = serializers.UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        '''Obtener y retornar el usuario autenticado'''
        return self.request.user