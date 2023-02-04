from django.shortcuts import render
from rest_framework import generics
from . import models, serializers

class TransactionHistoryView(generics.CreateAPIView):
    queryset = models.TransactionHistory.objects.all()
    serializer_class = serializers.TransactionHistorySerializer

class TransactionsView(generics.CreateAPIView):
    queryset = models.Transactions.objects.all()
    serializer_class = serializers.TransactionsSerializer

class SubscriptionsView(generics.CreateAPIView):
    queryset = models.Subscriptions.objects.all()
    serializer_class = serializers.SubscriptionsSerializer