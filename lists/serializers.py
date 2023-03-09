from rest_framework import serializers
from .models import List


class ListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj: List) -> dict:
        return {
            "id": obj.user.id,
            "username": obj.user.username,
        }

    class Meta:
        model = List
        fields = ["id", "name", "month", "year", "user"]
