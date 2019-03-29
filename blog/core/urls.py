from django.conf.urls import include
from django.urls import path
from rest_framework import routers


from django.conf.urls.static import static
from django.conf import settings

from core import views

router = routers.DefaultRouter()

router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path(r'api/v1/', include(router.urls)),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
