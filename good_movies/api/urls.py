from django.urls import path
from .views import RegisterView, LoginView, UserViewSet, LogoutView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserViewSet.as_view({'get': 'list'})),
    path('logout', LogoutView.as_view()),
]
