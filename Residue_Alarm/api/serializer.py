from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializa objeto de perfil de usuario'''
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'style': { 'input_type':'password'}
            }
        }
    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            password=validated_data['password']
        )

        return user
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.password = make_password(password)
