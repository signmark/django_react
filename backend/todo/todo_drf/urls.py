"""todo_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.schemas import openapi
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Todo App API",
        default_version='v1',
        description="Todo App API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dzhdanov@scnsoft.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

template_path = os.path.dirname(os.path.dirname(__file__))

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
