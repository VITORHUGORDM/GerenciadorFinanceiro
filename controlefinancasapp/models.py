from django.db import models
from django.utils import timezone
import calendar

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#3b82f6')
    is_income = models.BooleanField(default=False)
    icon = models.CharField(max_length=50, default='fas fa-tag')

    def __str__(self):
        return self.name

class Transaction(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def formatted_amount(self):
        return float(self.amount)

    @property
    def class_name(self):
        return self.__class__.__name__

class Income(Transaction):
    def get_display(self):
        return f"[+] {self.description}: R$ {self.amount}"

class Expense(Transaction):
    def get_display(self):
        return f"[-] {self.description}: R$ {self.amount}"

class Account:
    def __init__(self, owner="Usuário"):
        self._owner = owner

    @property
    def balance(self):
        incomes = sum(i.amount for i in Income.objects.all())
        expenses = sum(e.amount for e in Expense.objects.all())
        return float(incomes - expenses)
        
    @property
    def total_income(self):
        return float(sum(i.amount for i in Income.objects.all()))

    @property
    def total_expense(self):
        return float(sum(e.amount for e in Expense.objects.all()))

    def get_all_transactions(self):
        incomes = list(Income.objects.all().select_related('category'))
        expenses = list(Expense.objects.all().select_related('category'))
        transactions = incomes + expenses
        transactions.sort(key=lambda t: t.date, reverse=True)
        return transactions

    def get_expenses_by_category(self):
        expenses = Expense.objects.all().select_related('category')
        data = {}
        for e in expenses:
            cat_name = e.category.name if e.category else 'Outros'
            cat_color = e.category.color if e.category else '#94a3b8'
            if cat_name not in data:
                data[cat_name] = {'amount': 0, 'color': cat_color}
            data[cat_name]['amount'] += float(e.amount)
        return data
