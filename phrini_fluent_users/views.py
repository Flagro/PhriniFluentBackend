from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import PhriniFluentUser
from .serializers import PhriniFluentUserSerializer


# User Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def custom_user_list(request):
    if request.method == 'GET':
        users = PhriniFluentUser.objects.all()
        serializer = PhriniFluentUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PhriniFluentUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def custom_user_detail(request, pk):
    try:
        user = PhriniFluentUser.objects.get(pk=pk)
    except PhriniFluentUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhriniFluentUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhriniFluentUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
