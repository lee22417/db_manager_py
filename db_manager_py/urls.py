from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from usertest import views

router = routers.DefaultRouter()

# test 
router.register(r'users', views.UserViewSet) 
router.register(r'groups', views.GroupViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('test/', include('usertest.urls')), # test API

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token', obtain_jwt_token),
    path('api/token/verify', verify_jwt_token),
    path('api/token/refresh', refresh_jwt_token) 

]

