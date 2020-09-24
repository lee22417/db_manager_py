from django.core import serializers
from django.http import HttpResponse
from django.views.generic import View
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Question
from .serializers import QuestionSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class QuestionView(View):
	def get(self, request):
		questions = Question.objects.all()
		serializer = QuestionSerializer(questions, many=True)
		return JSONResponse(serializer.data)
	def post(self, request):
		data = JSONParser().parse(request)
		serializer = QuestionSerializer(data=data)
		if(serializer.is_valid()):
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		else:
			return JSONResponse(serializer.errors, status=400)