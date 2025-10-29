# criar um código que forneca uma api de clima 
# que informe a temperatura e a descrição do tempo em local específico

import requests 

api_key = '2a1ac38a32354cb7b19133643251408' # chave da api
cidade = input('Digite o nome da cidade: ').strip()
url= f'https://api.weatherapi.com/v1/current.json'

# parametros da requisição
parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt' #define portugues como lingua 
}

# fazer a requisição 
resposta = requests.get(url, params=parametros) # utilizamos o método get e informamos os parâmetros dessa requisição

# verificar se a requisição foi bem sucedida 

if resposta.status_code == 200:
    dados = resposta.json()  # convertendo a resposta JSON em um dicionário Python
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'Temperatura na cidade {cidade} é {temperatura}°C.')
    print(f'Descrição: {descricao}')

else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)