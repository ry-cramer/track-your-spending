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

# Classes for adding a new transaction to the database

class AddTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TransactionHistory
        fields = ('transaction_id', 'date', 'amount')

class NewTransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transactions
        fields = ('sub_id', 'name', 'category', 'necessity')

class NewSubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscriptions
        fields = ('type', 'frequency')

