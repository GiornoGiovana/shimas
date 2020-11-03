import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import User, Activity, MovieRecomment
from .serializers import UserSerializer, ActivitySerializer, MovieSeriaizer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .recommendation import get_movie_recomendations

# Create your views here.

class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def get_user_email(self, email):
        try:
            return User.objects.get(email=email)
        except:
            raise Http404

    def post(self, request):
        my_user = self.get_user_email(request.data["email"])
        if my_user:
            serializer = UserSerializer(my_user)
            if serializer.data["password"] == request.data["password"]:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                raise Http404
        return Response(Http404)

class UserDetail(APIView):

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data="wrong parameters") 

    def delete(self, request, pk):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActivityDetail(APIView):

    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ActivitySerializer(data=request.data)

        if request.data["activity_name"] == "Ver peliculas/series":
            movieserialize = MovieSeriaizer(data=self.convertData(request.data), many=True)
            if movieserialize.is_valid():
                movieserialize.save()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def convertData(self, mymovies: dict):
        movie_type = mymovies['activity_type']
        user_id = mymovies['user']

        movie_list = get_movie_recomendations(movie_type, 20)
        mylist = []
        for movie in movie_list:
            mylist.append({"user": user_id, "movie": movie['title'], "runtime": movie['runtime']})
        
        return mylist

class RecommendationList(APIView):

    def get(self, request, user_id):
        recomendation = MovieRecomment.objects.filter(user=user_id)
        serializer = MovieSeriaizer(recomendation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RecommendationDetail(APIView):
    def get_recomment(self,user_id , movie):
        try:
            return MovieRecomment.objects.filter(user=user_id, movie=movie)
        except:
            raise Http404

    def get(self, request, pk, movie):
        recommendation = self.get_recomment(pk, movie)
        serializer = MovieSeriaizer(recommendation, many=True)
        if serializer.data:
            return Response(serializer.data[0])
        raise Http404

class RecommendationFilter(APIView):
    def get_recomment(self,user_id , runtime):
        try:
            return MovieRecomment.objects.filter(user=user_id, runtime=runtime)
        except:
            raise Http404

    def get(self, request, pk, runtime):
        recommendation = self.get_recomment(pk, runtime)
        serializer = MovieSeriaizer(recommendation, many=True)
        if serializer.data:
            return Response(serializer.data)
        raise Http404

class DiscoverRecommendation(APIView):

    def discover(self):
        import random as rnd
        my_list = []
        genrs = ["Action", "Adventure", "Fantasy", "Science Fiction", "Crime", "Thriller", "Family"]
        random_choice = ""
        for i in range(3):
            my_choice = rnd.choice(genrs)
            if my_choice != random_choice:
                my_list.extend(get_movie_recomendations(my_choice, 8))
                random_choice = my_choice
        rnd.shuffle(my_list)
        return my_list
        

    def get(self, request):
        return HttpResponse(json.dumps(self.discover()), content_type="application/json")