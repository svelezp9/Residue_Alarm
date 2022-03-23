from rest_framework import serializers
from core.models import Residue


class ResidueSerializers(serializers.ModelSerializer):
    '''Serializador para objeto residuo'''
    class Meta:
        model = Residue
        fields = ('id','img_src','priority','status','lon','lat')
        read_only_Fields = ('id',)
    
    
