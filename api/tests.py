import json

# from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User, Activity
from .serializers import UserSerializer, ActivitySerializer

# Create your tests here.
class RegistrationTestCase(APITestCase):

    def test_signup(self):
        data = {"name": "testname", "email": "test@email.com",
                "password": "test_password"}
        response = self.client.post("/users/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_login(self):
        data = {"name": "testname", "email": "test@email.com",
                "password": "test_password"}
        res = self.client.post("/users/", data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        data = {"email": "test@email.com", "password":"test_password"}
        response = self.client.post('/users/login/', data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserCountTest(APITestCase):

    def test_count(self):
        data = {"name": "testname", "email": "test@email.com",
                "password": "test_password"}
        res = self.client.post("/users/", data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

class ProfileTestCase(APITestCase):

    def test_delete_profile(self):
        user = {"name": "user1", "email": "user1@email.com", "password": "test_password"}
        res = self.client.post("/users/", user)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED) 
        request = self.client.delete("/users/1/")
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_patch_profile(self):
        user = {"name": "user2", "email": "user2@email.com", "password": "test_password"}
        res = self.client.post("/users/", user)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED) 
        new_user = {"name": "newUser", "email": "newUser@email.com", "password": "new_password"}
        response = self.client.patch("/users/2/", new_user)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.json()['name'], "newUser")

    def test_profile(self):
        user = {"name": "user3", "email": "user3@email.com", "password": "test_password"}
        res = self.client.post("/users/", user)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED) 
        request = self.client.get("/users/3/")
        self.assertEqual(request.json()['name'], "user3")

class QuizTestCase(APITestCase):

    def test_quiz(self):
        user = {"name": "testname4", "email": "test4@email.com",
                "password": "test_password4"}
        res = self.client.post("/users/", user)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED) 
        data = {"activity_name": "Cocinar", "activity_type": "Tradicional",
                "user": 4}
        response =  self.client.post("/activity/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.assertEqual(Activity.objects.count(), 1)
