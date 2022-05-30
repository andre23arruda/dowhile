from django.urls import path, include
from rest_framework import routers
from .api.viewsets import (
    github_auth, github_token, signin_callback,
    MessagesViewSet, ProfilesViewSet
)

app_name = 'nlw_heat'

# router
router = routers.DefaultRouter()
router.register('messages', MessagesViewSet, basename='Messages')
router.register('profiles', ProfilesViewSet, basename='Profiles')

urlpatterns = [
    path('api/nlw_heat/', include(router.urls)),
    path('api/github-auth/', github_auth),
    path('github/', github_token),
    path('signin/callback/', signin_callback),
]
