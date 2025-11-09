def test_concluir_tarefa():
    todo = ToDoList()
    todo.adicionar_tarefa("Estudar PyTest", "Aprender asserts")
    todo.concluir_tarefa("Estudar PyTest")
    tarefas = todo.listar_tarefas()

    assert tarefas[0]["concluida"] is True
