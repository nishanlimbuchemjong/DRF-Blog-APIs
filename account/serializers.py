from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializer.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['username']).exist():
            raise serializers.ValidationError("username already taken.")

        return data
