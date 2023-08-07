import requests
#Atividade_M3S1
''' Para a atividade desta semana, você deverá criar um interator que irá iterar os dados da API (Application Interface) 
da tabela FIPE e retornar os carros de uma determinada marca de veículos (essa deverá ser passada para a classe 
que fará o papel de interator no momento da instanciação, neste caso use o ID de uma marca). '''

class Modelos:#Adicionando a classe Modelos que retorna os carros de uma determinada marca de veículos da TABELA FIPE usando UMA API"
    def __init__(self, codigo: str):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo}/modelos'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.modelos = data['modelos']
            self.passo = 0
            self.tamanho = len(self.modelos)

        else:
            print('FALHA AO CARREGAR')

    def __iter__(self):
        return self

    def __next__(self):
        if self.passo >= self.tamanho:
            raise StopIteration
        resposta = list(self.modelos)[self.passo]
        self.passo = self.passo + 1
        return resposta

solicitacao = Modelos('2')
for modelo in solicitacao:
    print(f'codigo: ', modelo['codigo'], modelo['nome'])