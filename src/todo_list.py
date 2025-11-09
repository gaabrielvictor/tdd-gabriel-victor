class ToDoList:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = {"titulo": titulo, "descricao": descricao, "concluida": False}
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.tarefas
