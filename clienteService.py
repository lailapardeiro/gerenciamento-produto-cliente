from api.clientesApiService import ClientesApiService

class Cliente:
    TODOS = "TODOS"
    SAIR = "SAIR"

    def __init__(self):
        self.clientesApi - ClientesApiService()
    

    def adicionarCliente(self):
        self.clientesApi.buscarClientes()

    def adicionarCliente(self):
        nome = input("Qual o nome do cliente que deseja adicionar? ")
        cpf = input("Qual o CPF do cliente que deseja adicionar? ")
        self.clientesApi.adicionarCliente(nome, cpf)

    def consultarClientePorId(self, id):
        try:
            id = int(id)
        except ValueError:
            print("Não foi digitado um número inteiro!")
            return None
        return next((cliente for cliente in clientes if cliente["id"] == id), None)

    def consultarClientePorNome(self, nome):
        return next((cliente for cliente in clientes if cliente["nome"].lower() == nome.lower()), None)

    def consultarClientePorCPF(self, cpf):
        return next((cliente for cliente in clientes if cliente["cpf"] == cpf), None)

    def consultarCliente(self, criterio=None):
        if criterio == "todos":
            for cliente in clientes:
                print(f"{cliente['id']} - {cliente['nome']} - {cliente['cpf']}")
        else:
            criterio = input("Deseja buscar por ID, nome ou CPF? (Digite 'todos' para retornar todos os clientes cadastrados): ").strip().lower()
            if criterio == "id":
                id = input("Digite o id do cliente que deseja buscar: ")
                cliente = self.consultarClientePorId(id)
            elif criterio == "nome":
                nome = input("Digite o nome do cliente que deseja buscar: ")
                cliente = self.consultarClientePorNome(nome)
            elif criterio == "cpf":
                cpf = input("Digite o CPF do cliente que deseja buscar: ")
                cliente = self.consultarClientePorCPF(cpf)
            elif criterio == "todos":
                cliente = "todos"
            else:
                print("Critério de busca inválido.")
                return

            if criterio == "todos":
                for cliente in clientes:
                    print(f"{cliente['id']} - {cliente['nome']} - {cliente['cpf']}")
            else:
                if cliente:
                    print(f"Dados do cliente: {cliente['id']} - {cliente['nome']} - {cliente['cpf']}")
                else:
                    print(f"Erro: Cliente com critério '{criterio}' não encontrado.")

    def editarCliente(self):
        while True:
            id = input("Digite o código do cliente que deseja editar ou digite 'Sair' para voltar ao menu: ")
            if id.upper() == "SAIR":
                break

            cliente_encontrado = self.clientesApi.consultarCliente(id)

            if cliente_encontrado is None:
                print("Erro: ID não encontrado. Veja a lista de clientes:")
                self.consultarCliente("todos")
                continue

            print(f"Dados atuais do cliente: {cliente_encontrado['id']} - {cliente_encontrado['nome']}")
            
            novo_nome = input("Digite o novo nome do cliente: ")
            novo_cpf = input("Digite o novo nome do cliente: ")

            if not novo_nome.strip():
                print("Erro: O nome do cliente não pode estar vazio.")
                continue
            if any(char.isdigit() for char in novo_nome):
                print("Erro: O nome do cliente não deve conter números.")
                continue
            cliente_encontrado['nome'] = novo_nome
            print(f"Cliente atualizado: {cliente_encontrado['id']} - {cliente_encontrado['nome']}")
            break


    def removerCliente(self):
        while True:
            id = input("Digite o código do cliente que deseja remover ou digite 'Sair' para voltar ao menu: ")
            if id.upper() == "SAIR":
                break
            cliente_encontrado = self.consultarClientePorId(id)
            if cliente_encontrado is None:
                print("Erro: ID não encontrado. Veja a lista de clientes:")
                self.consultarCliente("todos")
                continue
            clientes.remove(cliente_encontrado)
            print(f"Cliente {cliente_encontrado['nome']} removido com sucesso!")
            break