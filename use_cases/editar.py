from use_cases.adicionar import adicionarProduto
from use_cases.buscar import buscarPorCodigo
from repositorio import banco

def editarProduto(codigo, nome, categoria, preço):
    produto = buscarPorCodigo(codigo)
    if produto:
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preço
        print('Dados alterados com sucesso')
    else:
        print('Produto nao encontrado')

if __name__ == '__main__':
    adicionarProduto('mouse', 'perifericos', 199)
    editarProduto(1, 'teclado', 'perifericos', 199)
    print(banco)




