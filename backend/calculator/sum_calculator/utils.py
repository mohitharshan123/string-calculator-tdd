import re
from .exceptions import NegativeNumberException

class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.delimiters = [',', '\n']

    def calculate(self):
        # Handle custom delimiter if string starts with //
        if self.numbers.startswith("//"):
            self._parse_custom_delimiters()
                            
        numbers_array = self._get_numbers_array()
        self._validate_numbers(numbers_array)
        
        return sum(n for n in numbers_array if n <= 1000)
    
    def _parse_custom_delimiters(self):
        delimiter_end_index = self.numbers.index("\n")
        delimiter_part = self.numbers[2:delimiter_end_index]

        if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
            # Find all delimeters that would be inside []
            self.delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
        else:
            self.delimiters = [delimiter_part]

        self.numbers = self.numbers[delimiter_end_index + 1:]

        for delimiter in self.delimiters:
            # Replace delimiter with a , 
            self.numbers = self.numbers.replace(delimiter, ",")

    def _get_numbers_array(self):
        # Replace all occurances of \n with ,
        numbers_string = re.sub(r'[\r\n]+', ',', self.numbers)
        numbers_array = numbers_string.split(",")
                
        return [int(n) for n in numbers_array if n]
    
    
    def _validate_numbers(self, numbers):
        # Raise an exception if the input contains a negative number
        negatives = [n for n in numbers if n < 0]
        if negatives:
            raise NegativeNumberException(f"Negatives not allowed: {', '.join(map(str, negatives))}")
