#Atividade M3S3
'''formula para calculo do preço com e sem desconto
valor_com_desconto = valor_unitario * desconto * quantidade
valor_sem_desconto = valor_unitario * quantidade
'''
import pytest

def preco_sem_e_com_desconto(valor_unitario, quantidade):#função de calcula e retorna o custo com e sem desconto de um determinado produto e determinada quantidade
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


solicitacao = preco_sem_e_com_desconto(1000,90)
print(solicitacao)

def test_quant_entre_10_e_99():# Testa o resultado do calculo do preço com e sem desconto considerando a quantidade entre 10 e 99.
    valor = preco_sem_e_com_desconto(100, 15)
    assert valor == (1425, 1500)

def test_quant_entre_100_e_999():# Testa o resultado do calculo do preço com e sem desconto considerando a quantidade entre 100 e 999.
    valor = preco_sem_e_com_desconto(100, 110)
    assert valor == (9900,11000)

def test_quant_maior_que_999():# Testa o resultado do calculo do preço com e sem desconto considerando a quantidade maior do que 999.
    valor = preco_sem_e_com_desconto(100, 1100)
    assert valor == (93500,110000)


