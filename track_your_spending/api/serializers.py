from rest_framework import serializers
from . import models

class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TransactionHistory
        fields = ('id', 'transaction_id', 'date', 'amount')

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transactions
        fields = ('id', 'sub_id', 'name', 'category', 'necessity')

class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscriptions
        fields = ('id', 'type', 'frequency')