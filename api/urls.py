from django.urls import include, path
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('participant', ParticipantViewSet)
router.register('student', StudentViewSet)
router.register('level', LevelViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
