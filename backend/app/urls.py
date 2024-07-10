from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripsModelViewSet, EmailsToInviteModelViewSet, LinksModelViewSet

router = DefaultRouter()
router.register(r'trips', TripsModelViewSet)
router.register(r'emails', EmailsToInviteModelViewSet)
router.register(r'links', LinksModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
