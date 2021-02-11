from django.urls import include, path
from api.views import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('level', LevelView.as_view(), name="level"),
    path('board', LeaderboardView.as_view(), name="board"),
    path('reg', RegistrationAPI.as_view(), name='reg'),
    path('getposts', get_posts, name="posts"),
]
