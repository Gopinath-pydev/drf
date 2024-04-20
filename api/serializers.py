from rest_framework import serializers
from .models import todo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta():
        model = todo
        fields = ['id', 'name', 'description']
