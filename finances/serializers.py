from rest_framework import serializers
from .models import Finance


class FinanceSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Finance
        fields = ["id", "description", "value", "type", "category"]
