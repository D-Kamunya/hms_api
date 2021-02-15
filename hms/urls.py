"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="HMS API",
        #  version of the swagger doc
        default_version='v1',
        # first line that appears on the top of the doc
        description="Hospital Management System API",
    ),
    public=True,
)


def trigger_error(request):
    division_by_zero = 1 / 0

    
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('hms/', include('hmsapp.urls')),
    path('accounts/',include('users.urls')),
    path('payment/', include('mpesa_api.urls')),
]
