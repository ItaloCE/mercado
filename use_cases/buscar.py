from repositorio import banco
from use_cases.adicionar import adicionarProduto


def buscarPorCodigo(codigo: int) -> dict or None:
    for produto in banco:
        if codigo == produto['codigo']:
            return produto
    return None

if __name__ == '__main__':
    adicionarProduto('Mouse', 'Perifericos', 199)
    print(buscarPorCodigo(1))
    print(buscarPorCodigo(2))

