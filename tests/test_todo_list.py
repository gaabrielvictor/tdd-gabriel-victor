import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.todo_list import ToDoList


def test_remover_tarefa():
    todo = ToDoList()
    todo.adicionar_tarefa("Ler livro", "Clean Code")
    todo.remover_tarefa("Ler livro")
    tarefas = todo.listar_tarefas()

    assert len(tarefas) == 0
