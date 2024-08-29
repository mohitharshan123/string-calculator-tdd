from calculator.sum_calculator.utils import Calculator
from django.test import TestCase


class StringCalculatorTests(TestCase):
    def test_empty_string(self):
        calculator = Calculator("")
        self.assertEqual(calculator.add(), 0)

    def test_single_number(self):
        calculator = Calculator("1")
        self.assertEqual(calculator.add(), 1)

    def test_two_numbers(self):
        calculator = Calculator("1,2")
        self.assertEqual(calculator.add(), 3)

    def test_ignore_numbers_greater_than_1000(self):
        calculator = Calculator("2,1001,3")
        self.assertEqual(calculator.add(), 5)
