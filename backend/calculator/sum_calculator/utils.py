import re

class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.delimiters = [',', '\n']

    def add(self):                
        numbers_array = self._get_numbers_array()
        return sum(n for n in numbers_array if n <= 1000)
    
    def _get_numbers_array(self):
        numbers_string = re.sub(r'[\r\n]+', ',', self.numbers)
        numbers_array = numbers_string.split(",")
                
        return [int(n) for n in numbers_array if n]
