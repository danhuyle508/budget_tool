from django.urls import path
from .views import BudgetView,TransactionView, TransactionCreateView, BudgetCreateView

urlpatterns = [
    path('budget', BudgetView.as_view(), name='budget_view'),
    path('transaction/<int:id>', TransactionView.as_view(), name='transaction_detail'),
    path('transaction/add', TransactionCreateView.as_view(), name='Transaction_add'),
    path('budget/add', BudgetCreateView.as_view(), name='Budget_add'),
]