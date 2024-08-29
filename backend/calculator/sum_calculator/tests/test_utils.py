from calculator.sum_calculator.utils import Calculator
from django.test import TestCase


class StringCalculatorTests(TestCase):
    def test_empty_string(self):
        calculator = Calculator("")
        self.assertEqual(calculator.add(), 0)

    def test_single_number(self):
        calculator = Calculator("1")
        self.assertEqual(calculator.add(), 1)
