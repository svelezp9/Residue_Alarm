from tokenize import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializer,models , permissions

class descriptionAPI(APIView):

    def get(self,request,format=None):
        description = [
            'metodos get, post, delete'
        ]

        return Response({'message' : 'Hello', 'descriptionAPI':description})

class UserProfileViewSet(viewsets.ModelViewSet):
    '''Creación y update del user'''
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

class UserLoginApiView(ObtainAuthToken):
    '''Token de autenticación para el usuairo'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    