from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class ActivitySerializer(serializers.Serializer):
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    user = serializers.EmailField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    calories = serializers.IntegerField()
