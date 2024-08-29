import re
from .exceptions import NegativeNumberException

class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.delimiters = [',', '\n']

    def add(self):                
        numbers_array = self._get_numbers_array()
        self._validate_numbers(numbers_array)
        
        return sum(n for n in numbers_array if n <= 1000)
    
    def _get_numbers_array(self):
        numbers_string = re.sub(r'[\r\n]+', ',', self.numbers)
        numbers_array = numbers_string.split(",")
                
        return [int(n) for n in numbers_array if n]
    
    
    def _validate_numbers(self, numbers):
        negatives = [n for n in numbers if n < 0]
        if negatives:
            raise NegativeNumberException(f"negatives not allowed: {', '.join(map(str, negatives))}")
