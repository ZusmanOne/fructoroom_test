from django.urls import path
from .views import RegistrUserView

urlpatterns = [
    path('', RegistrUserView.as_view(), name='registr'),
]
