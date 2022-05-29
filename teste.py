produto = str(input('Qual o nome do produto? '))
categoria = str(input('Qual a categoria do produto? ')).lower()
qtde_estoque = int(input('Qual a quantidade em estoque? '))
if categoria == 'alimento':
    if qtde_estoque <= 50:
        print(f'Solicitar {produto} à equipe de compras, temos apenas {qtde_estoque} em estoque')
if categoria == 'bebidas':
    if qtde_estoque <= 75:
        print(f'Solicitar {produto} à equipe de compras, temos apenas {qtde_estoque} em estoque')
if categoria == 'limpeza':
    if qtde_estoque <= 30:
        print(f'Solicitar {produto} à equipe de compras, temos apenas {qtde_estoque} em estoque')