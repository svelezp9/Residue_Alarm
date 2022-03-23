from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Residue
from registers import serializers

class ResidueViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Residue.objects.all()
    serializer_class = serializers.ResidueSerializers

    def get_queryset(self):
        '''Retornar objetos para user autenticado'''
        return self.queryset.filter(user=self.request.user).order_by('priority')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

