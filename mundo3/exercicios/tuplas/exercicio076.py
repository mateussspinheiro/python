produtos = ('Lápis', 1.75, 
            'Borracha', 2.00, 
            'Caderno', 15.90, 
            'Estojo', 25.00, 
            'Transferidor', 4.20, 
            'Compasso', 9.99, 
            'Mochila', 120.32, 
            'Canetas', 22.30, 
            'Livro', 34.90)

centro = 'LISTAGEM DE PREÇOS'
centralizado = centro.center(30)
print('=' * 30)
print(centralizado)
print('=' * 30)

for ordem in range(0, len(produtos)):

    if ordem % 2 == 0:
        print(f'{produtos[ordem]:.<30}', end='')
    if ordem % 2 != 0:
        print(f'{produtos[ordem]:>7.2f}')

