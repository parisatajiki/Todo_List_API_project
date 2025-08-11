from rest_framework import serializers
from todo_app.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Todo
        fields = '__all__'