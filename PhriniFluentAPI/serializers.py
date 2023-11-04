from rest_framework import serializers
from .models import CustomUser, APIKey, Language, WordGroup, Word, WordDescription, UserWordGroup

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'telegram_handle', 'email', 'api_keys', 'word_groups']
        extra_kwargs = {
            'api_keys': {'read_only': True},
            'word_groups': {'read_only': True}
        }

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['id', 'user', 'api_key', 'date_issued', 'permissions', 'active']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language_tag', 'language_name']

class WordGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordGroup
        fields = ['id', 'name', 'language', 'description', 'is_global', 'users']

class WordSerializer(serializers.ModelSerializer):
    descriptions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Word
        fields = ['id', 'word_group', 'text', 'language', 'descriptions']

class WordDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordDescription
        fields = ['id', 'word', 'language', 'description_text']

class UserWordGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWordGroup
        fields = ['id', 'user', 'word_group', 'date_added']
