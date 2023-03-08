from rest_framework import serializers
from .models import List
from finances.serializers import FinanceSerializer


class ListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    finances = FinanceSerializer(many=True, read_only=True)

    def get_user(self, obj: List) -> dict:
        return {
            "id": obj.user.id,
            "username": obj.user.username,
        }

    class Meta:
        model = List
        fields = ["id", "name", "month", "year", "user", "finances"]
