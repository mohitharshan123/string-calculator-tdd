from calculator.sum_calculator.serializers import AddSerializer
from django.test import TestCase

class AddSerializerTests(TestCase):
    def test_valid_numbers(self):
        data = {'numbers': '1,2,3'}
        serializer = AddSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['numbers'], '1,2,3')