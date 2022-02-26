from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import User
from app.serializers import UserSerializer


@api_view(['GET'])
def user_list(request):
    """
    List all users, or create a new user
    """
    if request.method == 'GET':
        user = User.objects.all().order_by('-first_name')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def register(request):
    """
    Register a new user
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_profile(request, email):
    if request.method == 'GET':
        try:
            user = User.objects.get(email__exact=email)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-first_name')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
