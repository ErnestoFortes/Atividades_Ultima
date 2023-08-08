#Atividade M3_S3
'''formula para calculo do preço com e sem desconto
valor_com_desconto = valor_unitario * desconto * quantidade
valor_sem_desconto = valor_unitario * quantidade
'''

def preco_sem_e_com_desconto(valor_unitario, quantidade):
    desconto = 1
    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85
    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade
    return valor_com_desconto, valor_sem_desconto


solicitacao = preco_sem_e_com_desconto(500,15)
print(solicitacao)
