from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views


router = routers.DefaultRouter()

# default  viewsets
router.register(r'movies', views.MovieViewSet)
router.register(r'following', views.FollowingViewSets)
router.register(r'review', views.ReviewViewSet)


urlpatterns = [
     path('', include(router.urls)),
     path('token', jwt_views.TokenObtainPairView.as_view(),
          name='token_obtain_pair'),
     path('token/refresh', jwt_views.TokenRefreshView.as_view(),
          name='token_refresh'),
     path('register', views.RegisterView.as_view()),
     path('login', views.LoginView.as_view()),
     path('user', views.UserViewSet.as_view({'get': 'list'})),
     path('logout', views.LogoutView.as_view()),


    # custom
     path('addLikedList/<int:userId>/<str:imdbId>/', views.addLikedList),
     path('getUserLikedMovies/<int:id>/', views.getUserLikedMovies),
     path('getUserByUsername/<str:username>/', views.getUserByUsername),
     path('follow/<int:userId>/<str:username>/', views.follow),

     path('addWatchedList/<int:userId>/<str:imdbId>/',views.addWatchedList),
     path('getUserWatchedMovies/<int:id>/',views.getUserWatchedMovies),

     path('getMovieByImdbID/<str:imdbId>/', views.getMovieByImdbID),
     path('getReviewByMovieId/<str:imdbid>/',views.getReviewsByMovieId)
  
]
