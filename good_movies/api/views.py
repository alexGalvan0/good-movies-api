import datetime

import jwt
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.viewsets import ModelViewSet

from .models import Movie, User
from .serializers import MovieSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not Found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response
# userInfoView


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(id=self.request.user.id)
        return query_set


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "messege": "sucess"
        }
        return response


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['GET'])
    def getMoviesByUser(self, **kwargs):
        id = 3
        movies = Movie.objects.filter(user_id__id=id)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def addLikedList(request, userId, imdbId):
    movie = Movie.objects.get(imdbId=imdbId)
    user = User.objects.get(id=userId)

    if request.method == 'POST':
        movie.likes.add(user)
        movieSerializer = MovieSerializer(movie)
        return Response(movieSerializer.data)
    
    if request.method == 'DELETE':
        movie.likes.remove(user)
        movieSerializer = MovieSerializer(movie)
        return Response(movieSerializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def getUserLikedMovies(request, id):

    if request.method == 'GET':
        movies = Movie.objects.filter(likes__id=id)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getUserByUsername(request, username):
    user = User.objects.get(username=username)
    userSerializer = UserSerializer(user)
    return Response(userSerializer.data)