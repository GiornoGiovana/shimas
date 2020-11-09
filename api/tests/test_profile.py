from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import User

class ProfileTestCase(APITestCase):

    def test_get_profile_user(self):
        user = {"name": "user", "email": "user@email.com", "password": "testPassword"}
        res = self.client.post('/users/', user)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/users/2/')

        self.assertEqual(response.json()["name"], "user")
    
    def test_update_profile_user(self):
        user = {"name": "user", "email": "user@email.com", "password": "testPassword"}
        res = self.client.post('/users/', user)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        new_user = {"name": "newUser", "email": "newUser@email.com", "password": "new_password"}
        response = self.client.patch("/users/3/", new_user)

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        self.assertEqual(response.json()['name'], "newUser")

    def test_delete_profie_user(self):
        user = {"name": "user", "email": "user@email.com", "password": "testPassword"}
        res = self.client.post("/users/", user)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED) 
        request = self.client.delete("/users/1/")
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)