from django.db import models

class Subscriptions(models.Model):
    type = models.CharField(max_length=10)
    frequency = models.IntegerField()

class Transactions(models.Model):
    sub_id = models.ForeignKey(Subscriptions, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=False)
    category = models.CharField(max_length=50, unique=False)
    necessity = models.BooleanField()

class TransactionHistory(models.Model):
    transaction_id = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)