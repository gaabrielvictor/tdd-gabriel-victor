class ToDoList:
    def __init__(self):
        self._tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        self._tarefas.append({"titulo": titulo, "descricao": descricao, "concluida": False})

    def listar_tarefas(self):
        return list(self._tarefas)

    def concluir_tarefa(self, titulo):
        for tarefa in self._tarefas:
            if tarefa["titulo"] == titulo:
                tarefa["concluida"] = True
                break

    def remover_tarefa(self, titulo):
        self._tarefas = [t for t in self._tarefas if t["titulo"] != titulo]
