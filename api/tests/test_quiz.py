from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import User, Activity

class QuizTestCase(APITestCase):

    def test_quiz(self):
        user = {"name": "user", "email": "user@email.com", "password": "testPassword"}
        res = self.client.post("/users/", user)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED) 
        data = {"activity_name": "Cocinar", "activity_type": "Tradicional",
                "user": 4}
        response =  self.client.post("/activity/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.assertEqual(Activity.objects.count(), 1)
