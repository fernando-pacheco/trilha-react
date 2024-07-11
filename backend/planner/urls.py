from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripsViewSet, ParticipantsViewSet, ActivitiesViewSet, LinksViewSet

router = DefaultRouter()
router.register(r'trips', TripsViewSet, basename='trips')
router.register(r'participants', ParticipantsViewSet, basename='participants')
router.register(r'activities', ActivitiesViewSet, basename='activities')
router.register(r'links', LinksViewSet, basename='links')

urlpatterns = [
    path('trips/<uuid:tripId>/links/', LinksViewSet.as_view({'get': 'list', 'post': 'create'}), name='trip-links'),
    path('trips/<uuid:tripId>/activities/', ActivitiesViewSet.as_view({'get': 'list', 'post': 'create'}), name='trip-activities'),
    path('participants/<uuid:participantId>/', ParticipantsViewSet.as_view({'get': 'retrieve'}), name='participant-detail'),
    path('trips/<uuid:tripId>/participants/', ParticipantsViewSet.as_view({'get': 'list', 'post': 'create'}), name='trip-participants'),
    path('trips/<uuid:tripId>/', TripsViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='trip-detail'),
    path('trips/', TripsViewSet.as_view({'get': 'list', 'post': 'create'}), name='trip-list'),
    path('links/', LinksViewSet.as_view({'get': 'all', 'post': 'create'}), name='links-list'),
    path('participants/', ParticipantsViewSet.as_view({'get': 'all'}), name='participants-list'),
    path('activities/', ActivitiesViewSet.as_view({'get': 'all'}), name='activities-list'),
    path('', include(router.urls)),
]
