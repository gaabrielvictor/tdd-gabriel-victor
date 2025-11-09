from src.todo_list import ToDoList

def test_adicionar_tarefa():
    todo = ToDoList()
    todo.adicionar_tarefa("Estudar TDD", "Ler sobre o ciclo Red-Green-Refactor")
    tarefas = todo.listar_tarefas()

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar TDD"
