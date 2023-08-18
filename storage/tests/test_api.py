from rest_framework.test import APIClient
from storage.models import Page, Collection
from users.models import User
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestAuthenticatedEndpoint:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', email='test@mail.ru', password='123456')
        self.collection = Collection.objects.create(
            title='test collection',
            description='test text',
            user=self.user
        )
        self.page = Page.objects.create(
            title='test page',
            description='test text fot page',
            type='article',
            image='https://cdnn21.img.ria.ru/images/sharing/article/1741778019.jpg?8335530931629382628',
            link='https://ria.ru/20210718/proisshestviya-1741778019.html',
            user=self.user)

    def test_authorization_enpoint(self):
        url = reverse('rest_framework:login')
        headers = {'Email': 'test@mail.ru',
                   'Password': '123456'}
        response = self.client.get(url, headers=headers)
        assert response.status_code == 200

    def test_authenticated_page_list_endpoint(self):
        url = reverse('page-list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_page_endpoint(self):
        payload = {'link': 'https://ria.ru/20210718/proisshestviya-1741778019.html'}
        self.client.force_authenticate(user=self.user)
        url = reverse('create-page')
        response = self.client.post(url, data=payload, format="json")
        assert response.status_code == 201

    def test_authenticated_collection_detail_endpoint(self):
        url = reverse('page-detail', kwargs={'pk': self.collection.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        assert response.status_code == 200

    def test_update_page_endpoint(self):
        payload = {
            'title': 'newtest',
            'description': self.page.description,
            'type': self.page.type,
            'image': self.page.image,
            'link': self.page.link,
            'collection': self.collection.pk,
        }
        self.client.force_authenticate(user=self.user)
        url = reverse('page-detail', kwargs={'pk': self.page.pk})
        response = self.client.put(url, data=payload, format="json")
        assert response.status_code == 200

    def test_create_collection_endpoint(self):
        payload = {
            'title': 'test',
            'description': 'test text',
            "pages": []
        }
        self.client.force_authenticate(user=self.user)
        url = reverse('collection-list')
        response = self.client.post(url, data=payload, format="json")
        assert response.status_code == 201

    def test_destroy_collection(self):
        url = reverse('collection-detail', kwargs={'pk': self.collection.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        assert response.status_code == 204
