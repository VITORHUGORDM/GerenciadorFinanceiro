import json
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Income, Expense, Account, Category, Transaction

def init_categories():
    if Category.objects.count() == 0:
        categories = [
            {'name': 'Salário', 'color': '#10b981', 'is_income': True, 'icon': 'fas fa-money-bill'},
            {'name': 'Freelance', 'color': '#34d399', 'is_income': True, 'icon': 'fas fa-laptop-code'},
            {'name': 'Investimentos', 'color': '#0ea5e9', 'is_income': True, 'icon': 'fas fa-chart-line'},
            {'name': 'Moradia', 'color': '#ef4444', 'is_income': False, 'icon': 'fas fa-home'},
            {'name': 'Alimentação', 'color': '#f59e0b', 'is_income': False, 'icon': 'fas fa-utensils'},
            {'name': 'Transporte', 'color': '#3b82f6', 'is_income': False, 'icon': 'fas fa-car'},
            {'name': 'Saúde', 'color': '#ec4899', 'is_income': False, 'icon': 'fas fa-heartbeat'},
            {'name': 'Educação', 'color': '#8b5cf6', 'is_income': False, 'icon': 'fas fa-graduation-cap'},
            {'name': 'Lazer', 'color': '#a855f7', 'is_income': False, 'icon': 'fas fa-gamepad'},
            {'name': 'Outros', 'color': '#94a3b8', 'is_income': False, 'icon': 'fas fa-box'},
        ]
        for c in categories:
            Category.objects.create(**c)

def index(request):
    init_categories()
    account = Account()
    transactions = account.get_all_transactions()
    expenses_data = account.get_expenses_by_category()
    
    # Preparando dados das categorias para envio à view
    income_cats = list(Category.objects.filter(is_income=True).values('id', 'name'))
    expense_cats = list(Category.objects.filter(is_income=False).values('id', 'name'))
    
    context = {
        'account': account,
        'transactions': transactions,
        'income_categories_json': income_cats,
        'expense_categories_json': expense_cats,
        'expenses_data': expenses_data,
    }
    return render(request, 'controlefinancasapp/index.html', context)

class TransactionValidationError(Exception):
    """Exceção customizada para erros de validação nas transações."""
    pass

def add_transaction(request):
    if request.method == 'POST':
        t_type = request.POST.get('type')
        description = request.POST.get('description', '').strip()
        amount_str = request.POST.get('amount', '').strip()
        category_id = request.POST.get('category')
        
        try:
            # 1. Validação de Descrição
            if not description:
                raise TransactionValidationError("A descrição da transação não pode estar vazia.")
            
            # 2. Validação do Valor
            if not amount_str:
                raise TransactionValidationError("O valor da transação é obrigatório.")
            
            # Limpeza da máscara de moeda (Ex: "R$ 1.500,00" -> "1500.00")
            cleaned_amount = amount_str.replace('R$', '').replace('.', '').replace(',', '.').strip()
            
            try:
                amount = float(cleaned_amount)
            except ValueError:
                raise TransactionValidationError("O valor informado deve ser numérico e válido.")
            
            if amount <= 0:
                raise TransactionValidationError("O valor da transação deve ser estritamente maior que zero.")

            # 3. Validação de Categoria
            if not category_id:
                raise TransactionValidationError("É obrigatório selecionar uma categoria.")
                
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                raise TransactionValidationError("A categoria selecionada não existe no sistema.")
            
            # 4. Inserção baseada no Tipo
            if t_type == 'income':
                Income.objects.create(description=description, amount=amount, category=category)
                messages.success(request, 'Receita adicionada com sucesso!')
            elif t_type == 'expense':
                Expense.objects.create(description=description, amount=amount, category=category)
                messages.success(request, 'Despesa registrada com sucesso!')
            else:
                raise TransactionValidationError("Tipo de transação inválido.")
                
        except TransactionValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            # Tratamento genérico para qualquer outro erro inesperado (falha de banco, etc)
            messages.error(request, "Ocorreu um erro inesperado no servidor. Tente novamente mais tarde.")
            
        return redirect('index')
    
    return redirect('index')

def delete_transaction(request, tx_id):
    try:
        # Tenta buscar a transação antes de deletar
        tx = Transaction.objects.get(id=tx_id)
        tx_description = tx.description
        tx.delete()
        messages.warning(request, f'Transação "{tx_description}" removida com sucesso.')
    except Transaction.DoesNotExist:
        messages.error(request, 'Erro: A transação que você tentou deletar não foi encontrada.')
    except Exception as e:
        messages.error(request, "Ocorreu um erro interno ao tentar remover a transação.")
        
    return redirect('index')
