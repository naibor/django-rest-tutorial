from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    """
    list all snippets, create a snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update and delete a single snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIViews):
    """
    List all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """
    get user details
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
