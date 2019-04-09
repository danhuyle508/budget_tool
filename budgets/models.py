from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField()

class Transaction(models.Model):
    budget = models.ForeignKey(Budget,models.CharField(max_length=180, default='Untitled')
    amount = models.FloatField()
    description = models.CharField(max_length=1024, default='Empty')
    CHOICES = {
        (withdrawal, Withdrawal),
        (deposit, Deposit)

    } 
