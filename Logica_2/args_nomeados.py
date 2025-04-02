def exibe_ficha(**dados):
    print('----FICHA----')
    for chave, valor in dados.items():
        print(f'{chave.upper()} - {valor}')


exibe_ficha(nome='Gabriel Bergamini', estado_civil='casado')

