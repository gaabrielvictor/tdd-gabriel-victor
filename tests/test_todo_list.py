import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.todo_list import ToDoList


def test_concluir_tarefa():
    todo = ToDoList()
    todo.adicionar_tarefa("Estudar TDD", "Ler sobre o ciclo Red-Green-Refactor")
    todo.concluir_tarefa("Estudar TDD")
    tarefas = todo.listar_tarefas()

    assert tarefas[0]["concluida"] is True
