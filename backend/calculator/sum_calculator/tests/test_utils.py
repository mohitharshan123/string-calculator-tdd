from calculator.sum_calculator.exceptions import NegativeNumberException
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
    
    def test_handle_newline_as_delimiter(self):
        calculator = Calculator("1,2\n3")
        self.assertEqual(calculator.add(), 6)

    def test_handle_negative_numbers(self):
        calculator = Calculator("-1,2,-3")
        with self.assertRaises(NegativeNumberException) as exc:
            calculator.add()
        self.assertEqual(str(exc.exception), "negatives not allowed: -1, -3")