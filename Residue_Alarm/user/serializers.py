from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    ''' Serializador para objeto usuario'''

    class Meta:
        model = get_user_model()
        fields = ('email','password','name')
        extra_kwargs = {'password':{'write_only':True , 'min_length': 5}}

    def create(self, validated_data):
         ''' Crear nuevo usuario con clave encriptada y retornarlo'''

         return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    '''Serializador para token'''
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False
    )

    def validate(self,attrs):
        email = attrs.get('email')
        password = attrs.get('password')


        user = authenticate(
            request=self.context.get('request'),
            username = email,
            password=password
        )
        if not user:
            msg = _('Unable to aunthenticate')
            raise serializers.ValidationError(msg,code='authorization')
        
        attrs['user'] = user
        return attrs