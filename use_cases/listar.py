from repositorio import banco
from use_cases.adicionar import adicionarProduto

def listarProdutos():
    print('-----LISTA DE PRODUTOS -----')
    for produto in banco:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")

if __name__ == '__main__':
    adicionarProduto('Mouse', 'Perifericos', 155)
    adicionarProduto('Mousepad', 'Acessorios', 80)
    listarProdutos()

