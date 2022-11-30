from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from . import views
from .views import LoginView, LogoutView, RegisterView, UserViewSet

router = routers.DefaultRouter()


router.register(r'movie', views.MovieViewSet)


urlpatterns = [
    path('token', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserViewSet.as_view({'get': 'list'})),
    path('logout', LogoutView.as_view()),
]
