from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
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

# In progress----DOES NOT WORK YET

class AddTransactionView(APIView):
    def post(self, request, format=None):
        nst_serializer = serializers.NewSubscriptionTypeSerializer(data=request.data)
        if nst_serializer.is_valid():
            sub_type = nst_serializer.data.get('type')
            sub_freq = nst_serializer.data.get('frequency')
            queryset = models.Subscriptions.objects.filter(type=sub_type, frequency=sub_freq)
            if not queryset.exists():
                subscription = models.Subscriptions(type=sub_type, frequency=sub_freq)
                subscription.save()
            else:
                subscription = queryset[0]
        else:
            return Response({'Bad Request': 'Invalid Data...'}, status=status.HTTP_400_BAD_REQUEST)

        ntt_serializer = serializers.NewTransactionTypeSerializer(data=request.data)
        if ntt_serializer.is_valid():
            sub_id = serializers.SubscriptionsSerializer(subscription).data.get('id')
            name = ntt_serializer.data.get('name')
            category = ntt_serializer.data.get('category')
            necessity = ntt_serializer.data.get('necessity')
            queryset = models.Transactions.objects.filter(sub_id=sub_id, name=name, category=category, necessity=necessity)
            if not queryset.exists():
                transaction = models.Transactions(sub_id=sub_id, name=name, category=category, necessity=necessity)
                transaction.save()
            else:
                transaction = queryset[0]
        else:
            return Response({'Bad Request': 'Invalid Data...'}, status=status.HTTP_400_BAD_REQUEST)

        at_serializer = serializers.AddTransactionSerializer(data=request.data)
        if at_serializer.is_valid():
            trans_id = serializers.TransactionsSerializer(transaction).data.get('id')
            date = at_serializer.data.get('date')
            amount = at_serializer.data.get('amount')
            new_transaction = models.TransactionHistory(transaction_id=trans_id, date=date, amount=amount)
            new_transaction.save()
        else:
            return Response({'Bad Request': 'Invalid Data...'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializers.TransactionHistorySerializer(new_transaction).data, status=status.HTTP_201_CREATED)
