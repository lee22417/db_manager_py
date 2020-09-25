from django.urls import path, include 
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #path(r'^$', include (router.urls)),
    url(r'^board/$', views.QuestionList.as_view()),
    url(r'^board/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)