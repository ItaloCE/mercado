from repositorio import banco


codigo = 0

def gerarProduto(nome, categoria, preco):
    global codigo
    codigo += 1
    produto = {
        'codigo': codigo,
        'nome': nome,
        'categoria': categoria,
        'preco': preco
    }
    return produto


def adicionarProduto(nome, categoria, preco):
    produto = gerarProduto(nome, categoria, preco)
    banco.append(produto)
    print('Produto adicionado com sucesso!')


if __name__ == '__main__':
    adicionarProduto('Mouse', 'Perifericos', 199)
    adicionarProduto('Monitor', 'Perifericos', 990)

    print(banco)