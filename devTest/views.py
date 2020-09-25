from django.core import serializers
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.renderers import JSONRenderer

from .models import Question
from .serializers import QuestionSerializer

class QuestionView(generics.ListCreateAPIView):
        queryset = Question.objects.all()
        serializer_class = QuestionSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
        authentication_classes((JSONWebTokenAuthentication,))