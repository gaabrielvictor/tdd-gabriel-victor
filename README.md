# 🧪 Projeto: To-Do List (Desenvolvimento Guiado por Testes - TDD)

Este projeto foi desenvolvido como parte da atividade prática sobre **Desenvolvimento Guiado por Testes (TDD)**.  
O objetivo foi aplicar o ciclo **RED → GREEN → REFACTOR** para criar, testar e refatorar um sistema simples de gerenciamento de tarefas.

---

## 🚀 **Descrição do Projeto**

O sistema **To-Do List** permite gerenciar tarefas pessoais de forma simples.  
Cada tarefa possui um **título**, **descrição** e um **status** (pendente ou concluída).

### **Funcionalidades implementadas**
- ✅ Adicionar uma nova tarefa  
- ✅ Listar todas as tarefas  
- ✅ Concluir uma tarefa  
- 🛠️ (Planejado) Remover uma tarefa  

---
```
## ⚙️ **Estrutura do Projeto**

tdd-gabriel-victor/
│
├── pytest.ini
├── README.md
│
├── src/
│ ├── init.py
│ └── todo_list.py
│
└── tests/
└── test_todo_list.py
```
---

## 🧩 **Tecnologias Utilizadas**

- **Linguagem:** Python 3.13  
- **Biblioteca de Testes:** Pytest  
- **Ambiente Virtual:** venv  

---

## 🧠 **Ciclo TDD aplicado**

O desenvolvimento seguiu rigorosamente o ciclo **TDD (Test Driven Development)**:

1. **RED:** Escrever um teste que falha (antes da implementação).  
2. **GREEN:** Implementar o código mínimo necessário para o teste passar.  
3. **REFACTOR:** Refatorar o código, mantendo todos os testes passando.

### Exemplos de commits
- `cria teste para adicionar tarefa (RED)`
- `implementa método adicionar_tarefa (GREEN)`
- `refatora classe ToDoList mantendo testes passando (REFACTOR)`
- `cria teste e método para concluir tarefa`

---

## 🧰 **Como executar o projeto**

### 1️⃣ Clonar o repositório

git clone https://github.com/seuusuario/tdd-gabriel-victor.git
cd tdd-gabriel-victor


### 2️⃣ Criar e ativar o ambiente virtual
python -m venv venv


Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

### 3️⃣ Instalar as dependências
pip install pytest

### 4️⃣ Executar os testes
pytest -v


Se tudo estiver certo, o terminal mostrará algo assim:

tests/test_todo_list.py::test_adicionar_tarefa PASSED
tests/test_todo_list.py::test_concluir_tarefa PASSED

### 💬 Minha Experiência Utilizando TDD

Durante o desenvolvimento deste projeto, foi possível perceber como o TDD melhora a qualidade do código e reduz erros.
Seguir o ciclo RED → GREEN → REFACTOR ajuda a construir funcionalidades de forma mais segura e incremental.

Além disso, o processo torna o código mais limpo e fácil de manter, já que cada nova funcionalidade começa validada por testes automatizados.
O TDD me fez pensar primeiro no comportamento esperado do código, e só depois na implementação.

### 👨‍💻 Autor

Gabriel Victor
Projeto desenvolvido para a disciplina de ELABORAR PLANO DE TESTES E
VALIDAÇÃO DE UM SOFTWARE – UNIFACISA.
📅 Novembro de 2025
