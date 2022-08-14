from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    list all snippets, create a snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    #get all snippets
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #create a snippet
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
