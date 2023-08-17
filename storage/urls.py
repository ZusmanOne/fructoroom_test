from django.urls import path
from .views import (PageList,
                    CreatePageView,
                    PageDetail,
                    api_root,
                    CollectionList,
                    CollectionDetail)


urlpatterns = [
    path('', api_root, name='api'),
    path('create-page/', CreatePageView.as_view(), name='create'),
    path('pages/', PageList.as_view(), name='page-list'),
    path('page/<int:pk>/', PageDetail.as_view(), name='page-detail'),
    path('collections/', CollectionList.as_view(), name='collection-list'),
    path('collection/<int:pk>/', CollectionDetail.as_view(), name='collection-detail'),
]