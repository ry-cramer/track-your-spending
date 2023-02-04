from django.urls import path
from . import views

urlpatterns = [
    path('transaction-history', views.TransactionHistoryView.as_view(), name = 'Transaction History'),
    path('transactions', views.TransactionsView.as_view(), name = 'Transactions'),
    path('subscriptions', views.SubscriptionsView.as_view(), name = 'Subscriptions'),
]