from rest_framework import serializers
from .models import Language, WordGroup, WordGroupDescription, Word, WordDescription


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['language_name']


class WordGroupDescriptionSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = WordGroupDescription
        fields = ['description_text', 'language']


class WordGroupSerializer(serializers.ModelSerializer):
    descriptions = WordGroupDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = WordGroup
        fields = ['id', 'name', 'descriptions']


class WordDescriptionSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = WordDescription
        fields = ['description_text', 'language']


class WordSerializer(serializers.ModelSerializer):
    descriptions = WordDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Word
        fields = ['id', 'text', 'descriptions']
