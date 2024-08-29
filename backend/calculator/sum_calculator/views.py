from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AddSerializer

@api_view(['GET'])
def calculate(request):
    serializer = AddSerializer(data=request.data)
    if serializer.is_valid():
        numbers = serializer.validated_data['numbers']
        result = numbers
        return Response({'result': result})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

