#  Gerenciador Financeiro Pessoal

Um sistema de controle de gastos pessoais construído em Python (Django). O objetivo desta aplicação é facilitar a organização financeira, implementando conceitos de Programação Orientada a Objetos (POO) no backend.

---

## Funcionalidades

- **Dashboard:** Gráfico em anel exibindo as despesas divididas por categoria.
- **Categorias:** Organização das transações (ex: Salário, Moradia, Alimentação, Saúde, Lazer).
- **Máscara Monetária:** Formatação automática dos valores monetários inseridos.
- **Notificações:** Alertas na tela confirmando ações realizadas pelo usuário.
- **Validação:** Tratamento contra entradas inválidas (ex: categorias inexistentes ou valores negativos).

---

##  Onde a POO foi Aplicada?

O projeto atende aos requisitos utilizando o Django ORM:

1. **Herança:** O modelo `Transaction` funciona como classe base para `Income` (Receita) e `Expense` (Despesa), que herdam seus atributos.
2. **Encapsulamento:** Utilização do decorador `@property` na classe `Account` para o cálculo dos totais (Saldo, Receitas, Despesas), controlando o acesso a esses dados.
3. **Tratamento de Exceções:** Criação da classe `TransactionValidationError`, que herda de `Exception`, para tratar validações específicas da aplicação.
4. **Associação:** O relacionamento `ForeignKey` vincula a Transação a uma Categoria.

---

## Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação localmente:

### 1. Pré-requisitos

- Python instalado na máquina.

### 2. Instalar Dependências

No terminal, dentro da pasta do projeto, instale o Django:

```bash
pip install django
```

### 3. Iniciar o Servidor

Na raiz da pasta, execute o comando:
```bash
python manage.py runserver
```

### 4. Acessar o Sistema

Abra o navegador e acesse:
**http://127.0.0.1:8000/**

Divirta-se organizando suas finanças!
