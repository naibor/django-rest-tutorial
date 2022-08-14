from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404

class SnippetList(APIView):
    """
    List all snippets, create a new snippet
    """
    def get(self, request, format=None):
        #get all snippets from Snippet object
        snippets = Snippet.objects.all()
        #pass it throught the serializer
        serializer = SnippetSerializer(snippets, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        #serialize the data recieved
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
