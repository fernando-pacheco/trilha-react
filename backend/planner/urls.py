from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripsViewSet, ParticipantsViewSet, ActivitiesViewSet, LinksViewSet

router = DefaultRouter()
router.register(r'trips', TripsViewSet)
router.register(r'participants', ParticipantsViewSet)
router.register(r'activities', ActivitiesViewSet)
router.register(r'links', LinksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
