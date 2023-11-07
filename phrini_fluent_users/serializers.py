from rest_framework import serializers
from .models import PhriniFluentUser


class PhriniFluentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhriniFluentUser
        fields = ['id', 'username', 'telegram_handle', 'email']
