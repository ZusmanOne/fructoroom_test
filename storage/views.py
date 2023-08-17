from rest_framework.reverse import reverse
from rest_framework import permissions, generics
from .permissions import IsOwnerOrReadOnly
from .serializers import PageSerializer, CreatePageSerializer,CollectionSerializer
from .models import Page, Collection
from rest_framework.response import Response
from rest_framework.decorators import api_view
import opengraph


def get_page_data(url):
    og_data = opengraph.OpenGraph(url)
    return og_data


class CreatePageView(generics.CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = CreatePageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class PageList(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class CollectionList(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'pages': reverse('page-list', request=request, format=format),
        'collections': reverse('collection-list', request=request, format=format),
    })
