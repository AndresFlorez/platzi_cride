"""Users URLs"""

# Django
from django.urls import path, include

# Django rest framework
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# Views
from cride.circles.views import UserLoginAPIView


urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)