from django.shortcuts import render
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import request, HttpResponse
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from oauth2_provider import urls as oauth2_urls
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from ai.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT":  [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes =  [permissions.IsAuthenticated, TokenHasScope]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT":  [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('admin, OAuth2!')
