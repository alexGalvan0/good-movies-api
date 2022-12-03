from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views


router = routers.DefaultRouter()

# default  viewsets
router.register(r'movies', views.MovieViewSet)


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
    #     path('deleteUserLikedMovie/<id>/<movieId>/',views.deleteUserLikedMovie)
]
