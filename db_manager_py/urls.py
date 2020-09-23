from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('pretest/', include('usertest.urls')), # pretest API
    path('test/', include('devTest.urls')), # test API

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token', obtain_jwt_token),
    path('api/token/verify', verify_jwt_token),
    path('api/token/refresh', refresh_jwt_token) 

]

