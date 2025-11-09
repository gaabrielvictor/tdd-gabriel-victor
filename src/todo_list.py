class ToDoList:
    def __init__(self):
        self._tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        self._tarefas.append({"titulo": titulo, "descricao": descricao, "concluida": False})

    def listar_tarefas(self):
        return list(self._tarefas)
