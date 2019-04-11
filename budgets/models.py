from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField()

    def __repr__(self):
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)

class Transaction(models.Model):
    budget = models.ForeignKey(Budget,models.CharField(max_length=180, default='Untitled'))
    amount = models.FloatField()
    description = models.CharField(max_length=1024, default='Empty')

    STATES = {
        ('withdrawal', 'Withdrawal'),
        ('deposit', 'Deposit')
    } 
    status = models.CharField(
        max_length=16,
        choices=STATES,
        default='Withdrawal'
    )

    def __repr__(self):
        return '<Card: {} | {}>'.format(self.amount, self.status)

    def __str__(self):
        return '{} | {}'.format(self.amount, self.status)
