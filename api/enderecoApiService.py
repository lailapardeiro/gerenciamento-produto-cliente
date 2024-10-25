import http.client 
import json 
import pandas as pd

class EnderecoApiService:

    def consultarEnderecoIbge(self, cep=None):

        # Conectar ao servidor de API da Via Cep
        apiViaCep = http.client.HTTPSConnection("viacep.com.br")

        while True:
            # Solicitar o CEP ao usuário
            input('Digite o CEP para consultar o endereço: ')

            # Enviar uma requisiçao GET
            apiViaCep.request('GET', f'/ws/{cep}/json/')
            
            # Obter a resposta
            response = apiViaCep.getresponse()

            data = response.read().decode('utf-8')
            endereco = json.loads(data)

            endereco_simples = [
                {
                    'logradouro': endereco.get('logradouro'),
                    'bairro': endereco.get('bairro'),
                    'localidade': endereco.get('localidade'),
                    'uf': endereco.get('uf')
                }
            ]
            
            endereco_json = json.dumps(endereco_simples, indent=4)

            tabela = pd.DataFrame(endereco_json)
            print(tabela)
            break

servico = EnderecoApiService()
servico.consultarEnderecoIbge()



