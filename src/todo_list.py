class ToDoList:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = {"titulo": titulo, "descricao": descricao, "concluida": False}
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.tarefas

    def concluir_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa["titulo"] == titulo:
                tarefa["concluida"] = True
                break
