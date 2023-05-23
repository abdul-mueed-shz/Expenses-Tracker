from rest_framework import serializers

from apps.Expense.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id',
            'amount',
            'description',
            'user'
        ]
