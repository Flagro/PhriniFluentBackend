from rest_framework import serializers
from .models import Language, WordGroup, Word, WordDescription, UserWordGroup


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
