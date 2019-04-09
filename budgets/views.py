from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy
from .models import Budget, Transaction
from .forms import BudgetForm, TransactionForm

# Create your views here.

class BudgetView(LoginRequiredMixin,ListView):
    template_name = 'budgets/budget_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(category__user__username=self.request.user.username)
        return context  
class TransactionView(LoginRequiredMixin, DetailView):
    template_name = 'board/transaction_detail.html'
    model = Transaction
    context_object_name = 'transaction'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Transaction.objects.filter(transaction__user__username=self.request.user.username)      

# class TransactionCreateView(LoginRequiredMixin,CreateView):
#     template_name = ''
#     model = 
#     form_class = 
#     success_url = reverse_lazy('')