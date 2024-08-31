from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .exceptions import NegativeNumberException
from .serializers import AddSerializer
from .utils import Calculator


@api_view(['POST'])
def calculate(request):
    serializer = AddSerializer(data=request.data)
    if serializer.is_valid():
        numbers = serializer.validated_data['numbers']
        calculator = Calculator(numbers)
        try:
            result = calculator.calculate()
            return Response({'result': result})
        except NegativeNumberException as e:
            return Response({'numbers': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
