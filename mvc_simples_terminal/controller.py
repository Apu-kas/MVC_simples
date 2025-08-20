from model import modeloTarefa #Importa a função principal de "model"
from view import VerTarefa #Importa a função principal de "view"

class ControladorTarefa: #Classe para controlar as tarefas
    def __init__(self): #Inicializa o controlador
        self.model = modeloTarefa()  #Modelo de Tarefa
        self.view = VerTarefa()  #View de Tarefa

    def run(self):
        while True: #Loop principal
            choice = self.view.mostrar_menu() #Mostra o menu e obtém a escolha do usuário

            if choice == '1':
                self.add_tarefa()  #Adiciona uma nova tarefa
            elif choice == '2':
                self.listar_tarefas()  #Lista todas as tarefas
            elif choice == '3':
                self.deletar_tarefa()  #Deleta uma tarefa
            elif choice == '4':
                self.apaga_tudo()  #Apaga todas as tarefas
            elif choice == '0':
                self.view.mostrar_mensagem("Saindo do sistema...")  #Mensagem de saída
                break  # Encerra o loop
            else:  #Ação alternativa caso seja inserido um número inválido
                self.view.mostrar_mensagem("Opção inválida!")  #Mensagem de opção inválida

    def add_tarefa(self): #Função para adicionar uma nova tarefa
        tarefa = self.view.adicao_de_tarefas() #Obtém a tarefa a ser adicionada
        self.model.add_tarefa(tarefa) #Adiciona a tarefa ao modelo
        self.view.mostrar_mensagem("Tarefa adicionada com sucesso!") #Mensagem de confirmação

    def listar_tarefas(self): #Função para listar todas as tarefas
        tarefas = self.model.retorna_tarefa() #Obtém a lista de tarefas
        self.view.mostrar_tarefas(tarefas) #Mostra as tarefas na view

    def deletar_tarefa(self): #Função para remover uma tarefa
        tarefas = self.model.retorna_tarefa() #Obtém a lista de tarefas
        if not tarefas: #Verifica se há tarefas para remover
            self.view.mostrar_mensagem("Não há tarefas para remover!") #Mensagem de aviso
            return #Retorna se não houver tarefas

        self.view.mostrar_tarefas(tarefas) #Mostra as tarefas na view
        index = self.view.obter_numero_tarefa(len(tarefas)) #Obtém o índice da tarefa a ser removida
        removida = self.model.deletar_tarefa(index) #Remove a tarefa do modelo
        self.view.mostrar_mensagem(f"Tarefa removida: '{removida}'" if removida else "Tarefa não encontrada!") #Mensagem de confirmação e um "if" caso a tarefa não esteja ou já tenha saído da lista

    def apaga_tudo(self): #Função para apagar todas as tarefas
        if not self.model.retorna_tarefa(): #Verifica se há tarefas para limpar
            self.view.mostrar_mensagem("Não há tarefas para limpar!") #Mensagem de aviso
            return #Retorna se não houver tarefas

        self.model.apaga_tudo() #Apaga todas as tarefas do modelo
        self.view.mostrar_mensagem("Todas as tarefas foram removidas!") #Mensagem de confirmação