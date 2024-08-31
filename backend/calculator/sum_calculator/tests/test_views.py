from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CalculateViewTests(APITestCase):
    def test_calculate_success(self):
        url = reverse("calculate")
        data = {"numbers": "1, 2, 3"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"result": 6})

    def test_calculate_negative_number(self):
        url = reverse("calculate")
        data = {"numbers": "1, -2, 3"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("numbers", response.data)
        self.assertEqual(response.data["numbers"], "Negatives not allowed: -2")

    def test_calculate_number_greater_than_three_are_cubed(self):
        url = reverse("calculate")
        data = {"numbers": "1, 2, 3, 3, 3"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"result": 30})
