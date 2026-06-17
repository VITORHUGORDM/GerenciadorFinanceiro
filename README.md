# 💰 Gerenciador Financeiro Pessoal

Um sistema de controle de gastos pessoais super moderno, rápido e inteligente, construído em **Python (Django)**. Essa aplicação foi desenhada para facilitar a sua vida financeira, utilizando uma interface linda com *Dark Mode*, *Glassmorphism* e aplicando perfeitamente os melhores conceitos de **Programação Orientada a Objetos (POO)** no backend.

---

## ✨ Funcionalidades Principais

- **Dashboard Visual Interativo:** Gráfico em anel (Doughnut Chart) que mostra exatamente para onde seu dinheiro está indo com separação de cores.
- **Categorias Dinâmicas:** Organize tudo facilmente (Ex: Salário, Moradia, Alimentação, Saúde, Lazer).
- **Máscara Monetária Automática:** Digite os valores de forma natural e o sistema já insere o `R$` e a formatação brasileira em tempo real.
- **Sistema de Notificações (Toasts):** Avisos animados e elegantes saltam na tela confirmando suas ações (Adicionar, Deletar).
- **Blindado contra Erros:** Tratamento robusto contra entradas vazias, categorias inexistentes ou valores negativos no banco de dados.

---

## 🧩 Onde a POO foi Aplicada? (Explicação para a Atividade)

O projeto cumpre todos os requisitos exigidos com sobras, graças ao uso do Django ORM:

1. **Classes e Herança:** O modelo `Transaction` serve de classe Pai para `Income` (Receita) e `Expense` (Despesa), que herdam os atributos e a lógica de banco de dados nativamente.
2. **Encapsulamento (Properties):** Utilização do decorador `@property` na classe `Account` para calcular o Saldo, o Total de Receitas e o Total de Despesas. Isso garante que esses totais não sejam manipulados fora das regras de negócio.
3. **Tratamento de Exceções Customizadas:** Uma classe de erro própria `TransactionValidationError` herda de `Exception` para capturar especificamente as falhas de validação de negócios (Ex: valor negativo), tornando o código robusto.
4. **Associação (Composição):** O relacionamento no modelo (uso de `ForeignKey`) onde uma Transação "possui" uma Categoria, manipulando instâncias de categorias de forma dinâmica na criação dos relatórios (`get_expenses_by_category`).

---

## 🚀 Como Executar no seu Computador

O projeto é muito fácil de ser rodado. Você não precisa instalar bancos de dados complexos, basta seguir esses passos:

### 1. Pré-requisitos
Certifique-se de que você tem o **Python** instalado em sua máquina.

### 2. Instale as Dependências (Django)
Abra o seu terminal na pasta do projeto e digite:
```bash
pip install django
```

### 3. Inicie o Servidor Local
Ainda no terminal, na raiz da pasta `PROVAB2ROMES`, inicie o sistema rodando:
```bash
python manage.py runserver
```

### 4. Acesse o Sistema
Abra o seu navegador de preferência e digite o endereço abaixo:
👉 **http://127.0.0.1:8000/**

Divirta-se organizando suas finanças! 🎉
