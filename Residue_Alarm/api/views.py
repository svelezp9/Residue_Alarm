from email import message
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response

class descriptionAPI(APIView):

    def get(self,request,format=None):
        description = [
            'metodos get, post, delete'
        ]

        return Response({'message' : 'Hello', 'descriptionAPI':description})
