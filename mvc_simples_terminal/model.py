class modeloTarefa:
    def __init__(self):
        self._tarefas = []
    
    def add_tarefa(self, tarefa): #Função para adicionar uma nova tarefa
        if tarefa and tarefa.strip(): # Verifica se a tarefa não está vazia (em branco)
            self._tarefas.append(tarefa.strip()) # Usa "append" para colocar uma tarefa pro final da lista
    
    def retorna_tarefa(self): #Função para retornar uma "lista" com as tarefas
        return self._tarefas.copy() #Retorna uma cópia da "lista" de tarefas

    def deletar_tarefa(self, index): #Função para remover uma tarefa pelo índice
        if 0 <= index < len(self._tarefas): #Verifica se o índice está dentro do intervalo
            return self._tarefas.pop(index) # Usa o "pop" para retirar o número "index" da lista
        return None

    def apaga_tudo(self): #Função para limpar todas as tarefas
        self._tarefas.clear() # Usa "clear" para limpar a "lista" de tarefas