#ATIVIDADE DA SEMANA: M3S2
'''
Uma pessoa do seu time de desenvolvimento está escrevendo várias funções que calculam diferentes
formas de gerar juros. você deve escrever um decorator chamado decorator_imprimir, que será usado para a função chamada imprima os parâmetros:
capital, taxa e tempo, além do resultado da função.
'''
def decorador_imprimir(funcao):
    def dados(*args):
        dados_entrada = f'CAPITAL: {args[0]} TAXA: {args[1]} TEMPO: {args[2]}'
        calc_juro = funcao(*args)
        resultado= f'RESULTADO:  {calc_juro}'
        print(f'\n{dados_entrada} \n{resultado}')
    return dados


@decorador_imprimir
def juros_simples(capital, taxa, tempo):# Função que calcula o juro conforme dados de entrada: capital, taxa de juro e o tempo de amortização
    return capital * (taxa/100) * tempo


juros_simples(1000, 5, 6)