# Ana Beatriz Queiroz Costa

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto, quantidade=1):
        self.itens.append({'produto': produto, 'quantidade': quantidade})

    def remover(self, produto):
        self.itens = [item for item in self.itens if item['produto'] != produto]

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item['produto'].preco * item['quantidade']
        return total


# Produtos
produtos_cadastrados = {}

def cadastrar_produto():
    print('\n---✧CADASTRE O NOVO PRODUTO✧---')
    nome = input("Nome do produto: ").strip()
    if nome in produtos_cadastrados:
        print("Este produto já está cadastrado!")
        return

    try:
        preco = float(input("Preço do produto: R$ "))
        produtos_cadastrados[nome] = Produto(nome, preco)
        print(f"Produto '{nome}' cadastrado com sucesso!!")
    except ValueError:
        print("Por favor, insira valores válidos para o preço.")

def remover_produto():
    print('\n---✧REMOVA UM PRODUTO✧---')
    nome = input("Nome do produto: ").strip()
    if nome not in produtos_cadastrados:
        print("Este produto não está cadastrado!!")
        return


    del produtos_cadastrados[nome]
    print(f"Produto '{nome}' removido com sucesso!!")


def listar_produtos():
    if not produtos_cadastrados:
        print("Nenhum produto cadastrado.")
        return

    print("\n---✧LISTA DE PRODUTOS CADASTRADOS✧---")
    for nome, produto in produtos_cadastrados.items():
        print(f"- {produto.nome}: R${produto.preco:.2f}")

# Carrinho

def adicionar_ao_carrinho(carrinho):
    listar_produtos()
    nome_produto = input('Digite o nome do produto para adicionar ao carrinho: ')
    if nome_produto in produtos_cadastrados:
        produto = produtos_cadastrados[nome_produto]
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")
            carrinho.adicionar(produto, quantidade)
            print(f"{quantidade} unidades de {produto.nome} adicionadas ao carrinho.")
        except ValueError as e:
            print(f"Erro ao adicionar ao carrinho: {e}")
    else:
        print("Produto não encontrado.")
    return carrinho

def exibir_carrinho(carrinho):
    if not carrinho.itens:
        print("O carrinho está vazio.")
        return

    print("\n---✧CONTEÚDO DO CARRINHO✧---")
    for item in carrinho.itens:
        produto = item['produto']
        quantidade = item['quantidade']
        print(f"- {produto.nome} x{quantidade}: R${produto.preco * quantidade:.2f}")

def remover_do_carrinho(carrinho):
    nome_produto = input("Digite o nome do produto para remover do carrinho: ")
    produto_para_remover = None
    for item in carrinho.itens:
        if item["produto"].nome == nome_produto:
            produto_para_remover = item["produto"]
            break
    if produto_para_remover:
        carrinho.remover(produto_para_remover)
        print(f"{nome_produto} removido do carrinho.")
    else:
        print("Produto não encontrado no carrinho.")

# Menus
def exibir_menu_principal():
    print("\n---✧BEM VINDO✧---")
    print("1 - Login Cliente")
    print("2 - Login Equipe")

def exibir_menu_cliente():
    print("\n---✧MENU PRINCIPAL✧---")
    print("1 - Adicionar Produto ao Carrinho")
    print("2 - Exibir Carrinho")
    print("3 - Calcular Total do Carrinho")
    print("4 - Remover Produto do Carrinho")
    print("0 - Sair")

def exibir_menu_equipe():
    print("\n---✧MENU PRINCIPAL✧---")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Remover Produto")
    print("0 - Sair")

carrinho = Carrinho()

while True:
    exibir_menu_principal()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        while True:
            exibir_menu_cliente()
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                carrinho = adicionar_ao_carrinho(carrinho)
            elif opcao == '2':
                exibir_carrinho(carrinho)
            elif opcao == '3':
                print(f"Total do carrinho: R${carrinho.calcular_total():.2f}")
            elif opcao == '4':
                remover_do_carrinho(carrinho)
            elif opcao == '0':
                print("Saindo... Tchauuuu (❁´◡`❁)")
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif opcao == '2':
        while True:
            exibir_menu_equipe()
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cadastrar_produto()
            elif opcao == '2':
                listar_produtos()
            elif opcao == '3':
                remover_produto()
            elif opcao == '0':
                print('Muito obrigrado por utilizar o nosso sistema')
                break
            else:
                print("Opção inválida. Tente novamente.")

    else:
        print("Opção inválida. Tente novamente.")