from rest_framework import serializers
from .models import Page, Collection
from opengraph import OpenGraph
from django.db import transaction


def get_page_data(url):
    og_data = OpenGraph(url)
    return og_data


class CreatePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('link',)

    @transaction.atomic
    def save(self, *args, **kwargs):
        url = self.validated_data['link']
        page_data = get_page_data(url)
        page = Page(
            title=page_data.title,
            description=page_data.description,
            type=page_data.type,
            user=self.context['request'].user,
            link=page_data.url,
            image=page_data.image,
        )
        page.save()
        return page


class PageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Page
        fields = ['url', 'id', 'title', 'description', 'type', 'image', 'link']


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    pages = serializers.PrimaryKeyRelatedField(
        queryset=Page.objects.all(),
        many=True,
        read_only=False
    )

    class Meta:
        model = Collection
        fields = ['url', 'title', 'description', 'pages', 'pages']
