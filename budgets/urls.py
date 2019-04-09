from django.urls import path
from .views import BudgetView

urlpatterns = [
    path('budget', BudgetView.as_view(), name='budget_view'),
    path('transaction/<int:id>', TransactionView.as_view(), name='transaction_detail'),
]