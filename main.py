from use_cases.adicionar import adicionarProduto
from use_cases.listar import listarProdutos
from use_cases.buscar import buscarPorCodigo
from use_cases.editar import editarProduto
from use_cases.deletar import deletarProduto

def menu():
    print('---BEM VINDO AO MENU---')
    print('1 - Adicionar produto')
    print('2 - Editar produto')
    print('3 - Buscar produto')
    print('4 - Deletar produto')
    print('5 - Listar todos os produtos')
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        nome = input('Digite o nome do produto: ')
        categoria = input('Digite a categoria do produto: ')
        preco = float(input('Digite o preço do produto: '))
        adicionarProduto((nome, categoria, preco))
    elif opcao == 2:
        codigo = int(input('Digite o codigo do produto: '))
        nome = input('Digite o nome do produto: ')
        categoria =  input('Digite a categoria do produto: ')
        preco = float(input('Digite o preço do produto: '))
        editarProduto(codigo, nome, categoria, preco)
    elif opcao == 3:
        codigo = int(input('Digite o codigo do produto: '))
        buscarPorCodigo(codigo)
    elif opcao == 4:
        codigo = int(input('Digite o codigo do produto: '))
        deletarProduto(codigo)
    elif opcao == 5:
        listarProdutos()









