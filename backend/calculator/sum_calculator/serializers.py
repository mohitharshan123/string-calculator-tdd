from rest_framework import serializers

class AddSerializer(serializers.Serializer):
    numbers = serializers.CharField()