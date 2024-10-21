produtos = [
    {"id": 1, "descricao": "Prato", "codigo_barra": "12345"},
    {"id": 2, "descricao": "Caneca", "codigo_barra": "67890"},
    {"id": 3, "descricao": "Garfo", "codigo_barra": "13579"},
    {"id": 4, "descricao": "Faca", "codigo_barra": "24680"}
]

class Produto:
    TODOS = "TODOS"
    SAIR = "SAIR"

    def adicionarProduto(self):
        descricao = input("Qual a descrição do produto que deseja adicionar? ")
        codigo_barra = input("Qual o código de barra do produto que deseja adicionar? ")
        if not descricao.strip():
            print("Erro: A descrição do produto não pode estar vazia.")
            return
        proximoId = len(produtos) + 1
        while next((produto for produto in produtos if produto["id"] == proximoId), None) is not None:
            proximoId += 1
        produtos.append({"id": proximoId, "descricao": descricao, "codigo_barra": codigo_barra})
        print(f"Produto {descricao} foi adicionado à lista de Produtos com o ID {proximoId}")

    def consultarProdutoPorId(self, id):
        try:
            id = int(id)
        except ValueError:
            print("Não foi digitado um número inteiro!")
            return None
        return next((produto for produto in produtos if produto["id"] == id), None)

    def consultarProdutoPorDescricao(self, descricao):
        return next((produto for produto in produtos if produto["descricao"].lower() == descricao.lower()), None)

    def consultarProdutoPorCodigoBarra(self, codigo_barra):
        return next((produto for produto in produtos if produto["codigo_barra"] == codigo_barra), None)

    def consultarProduto(self, criterio=None):
        if criterio == "todos":
            for produto in produtos:
                print(f"{produto['id']} - {produto['descricao']} - {produto['codigo_barra']}")
        else:
            criterio = input("Deseja buscar por ID, descrição ou código de barra? (Digite 'todos' para retornar todos os produtos cadastrados): ").strip().lower()
            if criterio == "id":
                id = input("Digite o id do produto que deseja buscar: ")
                produto = self.consultarProdutoPorId(id)
            elif criterio == "descricao":
                descricao = input("Digite a descrição do produto que deseja buscar: ")
                produto = self.consultarProdutoPorDescricao(descricao)
            elif criterio == "codigo_barra":
                codigo_barra = input("Digite o código de barra do produto que deseja buscar: ")
                produto = self.consultarProdutoPorCodigoBarra(codigo_barra)
            elif criterio == "todos":
                produto = "todos"
            else:
                print("Critério de busca inválido.")
                return

            if criterio == "todos":
                for produto in produtos:
                    print(f"{produto['id']} - {produto['descricao']} - {produto['codigo_barra']}")
            else:
                if produto:
                    print(f"Dados do produto: {produto['id']} - {produto['descricao']} - {produto['codigo_barra']}")
                else:
                    print(f"Erro: Produto com critério '{criterio}' não encontrado.")

    def editarProduto(self):
        while True:
            id = input("Digite o código do produto que deseja editar ou digite 'Sair' para voltar ao menu: ")
            if id.upper() == "SAIR":
                break
            produto_encontrado = self.consultarProdutoPorId(id)
            if produto_encontrado is None:
                print("Erro: ID não encontrado. Veja a lista de produtos:")
                self.consultarProduto("todos")
                continue
            print(f"Dados atuais do produto: {produto_encontrado['id']} - {produto_encontrado['descricao']}")
            nova_descricao = input("Digite a nova descrição do produto: ")
            if not nova_descricao.strip():
                print("Erro: A descrição do produto não pode estar vazia.")
                continue
            produto_encontrado['descricao'] = nova_descricao
            print(f"Produto atualizado: {produto_encontrado['id']} - {produto_encontrado['descricao']}")
            break

    def removerProduto(self):
        while True:
            id = input("Digite o código do produto que deseja remover ou digite 'Sair' para voltar ao menu: ")
            if id.upper() == "SAIR":
                break
            produto_encontrado = self.consultarProdutoPorId(id)
            if produto_encontrado is None:
                print("Erro: ID não encontrado. Veja a lista de produtos:")
                self.consultarProduto("todos")
                continue
            produtos.remove(produto_encontrado)
            print(f"Produto {produto_encontrado['descricao']} removido com sucesso!")
            