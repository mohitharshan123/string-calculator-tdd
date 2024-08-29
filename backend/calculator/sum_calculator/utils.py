

class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.delimiters = [',', '\n']

    def add(self):
        numbers_array = self.numbers.split(",") 
                
        return sum(int(n) for n in numbers_array if n)
    