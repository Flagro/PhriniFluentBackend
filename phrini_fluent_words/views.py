from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
import random
from .models import WordGroup, Word, Language
from .permissions import IsOwner
from .serializers import WordGroupSerializer, WordSerializer


# Helper function to get the language or default
def get_language_or_default(request):
    default_language_code = getattr(settings, 'DESCRIPTIONS_LANGUAGE', 'english')
    language_name = request.query_params.get('language', default_language_code)
    language, _ = Language.objects.get_or_create(language_name=language_name)
    return language


@api_view(['GET'])
@permission_classes([AllowAny])
def public_word_group_list(request):
    language = get_language_or_default(request)
    word_groups = WordGroup.objects.filter(
        is_global=True,
        descriptions__language=language
    ).distinct()
    serializer = WordGroupSerializer(word_groups, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwner])
def private_word_group_list(request):
    language = get_language_or_default(request)
    word_groups = WordGroup.objects.filter(
        owner=request.user,
        descriptions__language=language
    ).distinct()
    serializer = WordGroupSerializer(word_groups, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def random_word_from_group(request, group_id):
    word_group = get_object_or_404(WordGroup, id=group_id)
    if word_group.is_global or (word_group.owner and word_group.owner == request.user):
        words = word_group.words.all()
        random_word = random.choice(words) if words else None
        if random_word:
            serializer = WordSerializer(random_word)
            return Response(serializer.data)
        return Response({'error': 'No words in the group'}, status=404)
    return Response({'error': 'You do not have permission to view this group'}, status=403)


@api_view(['POST'])
@permission_classes([AllowAny])
def word_similarity(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    answer_text = word.text
    input_text = request.data.get('text', '')
    # Here you will implement your similarity logic.
    # For now, let's just return a dummy similarity score.
    similarity_score = 100 if answer_text.lower().strip() == input_text.lower().strip() else 0
    return Response({'similarity': similarity_score})
