"""View module for handling requests for users"""

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from invEStiGuideAPI.serializers.user_serializer import UserSerializer

class UserView(ViewSet):
    """Handles requests for Users"""
    
# get a user
    def retrieve(self, request, pk):
        """Handle GET requests for single user
        
        Returns: 
            Response -- JSON serialized user
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except ObjectDoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


# get all users
    def list(self, request):
        """Handle GET requests to get all users
        
        Returns:
            Response -- JSON serialized list of users
        """
        
        users = User.objects.all().order_by('username')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# update a user