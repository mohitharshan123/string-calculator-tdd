from calculator.sum_calculator.exceptions import NegativeNumberException
from calculator.sum_calculator.utils import Calculator
from django.test import TestCase


class StringCalculatorTests(TestCase):
    def test_empty_string(self):
        calculator = Calculator("")
        self.assertEqual(calculator.calculate(), 0)

    def test_single_number(self):
        calculator = Calculator("1")
        self.assertEqual(calculator.calculate(), 1)

    def test_two_numbers(self):
        calculator = Calculator("1,2")
        self.assertEqual(calculator.calculate(), 3)

    def test_ignore_numbers_greater_than_1000(self):
        calculator = Calculator("2,1001,3")
        self.assertEqual(calculator.calculate(), 5)

    def test_handle_newline_as_delimiter(self):
        calculator = Calculator("1,2\n3")
        self.assertEqual(calculator.calculate(), 6)

    def test_handle_negative_numbers(self):
        calculator = Calculator("-1,2,-3")
        with self.assertRaises(NegativeNumberException) as exc:
            calculator.calculate()
        self.assertEqual(str(exc.exception), "Negatives not allowed: -1, -3")

    def test_handle_custom_delimiter(self):
        calculator = Calculator("//;\n1;2;3")
        self.assertEqual(calculator.calculate(), 6)

    def test_handle_multiple_custom_delimiters(self):
        calculator = Calculator("//[*][%]\n1*2%3")
        self.assertEqual(calculator.calculate(), 6)

    def test_handle_long_delimiters(self):
        calculator = Calculator("//[***][%%%]\n1***2%%%3")
        self.assertEqual(calculator.calculate(), 6)

    def test_edge_case_with_only_delimiters(self):
        calculator = Calculator("//;\n;;;")
        self.assertEqual(calculator.calculate(), 0)

    def test_cube_numbers(self):
        calculator = Calculator("1, 2, 3, 3, 3")

        self.assertEqual(calculator.calculate(), 30)
    
    def test_cube_numbers_for_more_than_one_number(self):
        calculator = Calculator("1, 2, 3, 3, 3, 2, 2")

        self.assertEqual(calculator.calculate(), 36)
