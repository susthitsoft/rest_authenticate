from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import HomeTemplateView, TestAuthView
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_auth/', TestAuthView.as_view(), name='test_auth', ),
    url(r'^rest-auth/', include('rest_auth.urls')),
    path(r'', HomeTemplateView.as_view(), name='home', ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
