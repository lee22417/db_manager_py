from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.renderers import JSONRenderer

from django.contrib.auth.models import User, Group
from usertest.serializers import UserSerializer, GroupSerializer

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def userlist(request):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    users = serializers.serialize('json',queryset)
    return HttpResponse(users, content_type="text/json_comment_filtered")

class UserViewSet(viewsets.ModelViewSet):
    #API endpoint that allows users to be viewed or edited.
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    #API endpoint that allows groups to be viewed or edited.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]  
