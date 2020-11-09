from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import User

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