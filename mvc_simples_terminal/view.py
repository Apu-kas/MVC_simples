class VerTarefa:
    @staticmethod #Utilizado para mostrar uma função estática
    def mostrar_menu(): #Função para mostrar o menu principal
        print("\n--- MENU PRINCIPAL ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Limpar todas as tarefas")
        print("0. Sair")
        return input("Escolha uma opção: ") #Recebe o valor (opção) para definir a tarefa
    
    @staticmethod #Utilizado para mostrar uma função estática
    def mostrar_tarefas(tarefas): #função para mostrar a lista de tarefas
        print("\n--- SUAS TAREFAS ---")
        if not tarefas: #Verifica se tem tarefas na lista
            print("Nenhuma tarefa cadastrada.") #Resultado caso não tenha tarefas
        else:
            for i, tarefa in enumerate(tarefas, 1): #Usa um para/for para percorrer a lista e enumera cada elemento (tarefa) da lista
                print(f"{i}. {tarefa}") #Utilza o print para mostrar a lista enumerada das tarefas

    @staticmethod #Utilizado para mostrar uma função estática
    def adicao_de_tarefas(): #Função para adicionar uma nova tarefa
        return input("\nDigite a nova tarefa: ") #Recebe a nova tarefa do usuário

    @staticmethod #Utilizado para mostrar uma função estática
    def obter_numero_tarefa(max_index): #Função para obter o número da tarefa que será removida
        while True: #Faz um loop infinito com "while" até receber uma entrada válida
            try:
                index = int(input(f"\nDigite o número da tarefa a remover (1-{max_index}): ")) #Recebe o número da tarefa e faz a validação para remoção da tarefa por uma subtração no parâmetro "max_index"
                if 1 <= index <= max_index: #Verifica se o número da tarefa está dentro do intervalo válido
                    return index - 1 #Retorna o índice da tarefa a ser removida
                print("Número inválido!") #Mensagem exibida quando o número da tarefa é inválido
            except ValueError: #Tratamento de erro para valores inválidos
                print("Por favor, digite um número válido!") #Mensagem exibida quando a entrada não é um número

    @staticmethod #Utilizado para mostrar uma função estática
    def mostrar_mensagem(message):
        print(f"\n{message}")