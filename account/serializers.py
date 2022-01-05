from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = serializers.ALL_FIELDS

    def get_password(self,object):
        return ("Fuck You")