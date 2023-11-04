from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser, APIKey, Language, WordGroup, Word, WordDescription, UserWordGroup
from .serializers import (CustomUserSerializer, APIKeySerializer, LanguageSerializer,
                          WordGroupSerializer, WordSerializer, WordDescriptionSerializer,
                          UserWordGroupSerializer)

# User Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # or use [AllowAny] if you want it to be accessible without authentication
def custom_user_list(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def custom_user_detail(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# APIKey Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def apikey_list(request):
    if request.method == 'GET':
        apikeys = APIKey.objects.filter(user=request.user)
        serializer = APIKeySerializer(apikeys, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = APIKeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def apikey_detail(request, pk):
    try:
        apikey = APIKey.objects.get(pk=pk, user=request.user)
    except APIKey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = APIKeySerializer(apikey)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = APIKeySerializer(apikey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apikey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Language Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def language_list(request):
    if request.method == 'GET':
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def language_detail(request, pk):
    try:
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# WordGroup Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def wordgroup_list(request):
    if request.method == 'GET':
        wordgroups = WordGroup.objects.all()
        serializer = WordGroupSerializer(wordgroups, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WordGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def wordgroup_detail(request, pk):
    try:
        wordgroup = WordGroup.objects.get(pk=pk)
    except WordGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordGroupSerializer(wordgroup)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WordGroupSerializer(wordgroup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wordgroup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Word Views
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def word_list(request):
    if request.method == 'GET':
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def word_detail(request, pk):
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# WordDescription Views
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def word_description_list(request):
    if request.method == 'GET':
        word_descriptions = WordDescription.objects.all()
        serializer = WordDescriptionSerializer(word_descriptions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WordDescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def word_description_detail(request, pk):
    try:
        word_description = WordDescription.objects.get(pk=pk)
    except WordDescription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordDescriptionSerializer(word_description)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WordDescriptionSerializer(word_description, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        word_description.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
