import requests
import os
from dotenv import load_dotenv

load_dotenv()

class AssistenteMaratona:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.base_url = "http://www.omdbapi.com/"

    def buscar_serie(self, nome_da_serie):
        """Método com parâmetros (Seção V.1.c)"""
        try:
            params = {"apikey": self.api_key, "t": nome_da_serie, "type": "series"}
            response = requests.get(self.base_url, params=params)
            dados = response.json()

            if dados.get("Response") == "True":
                return {
                    "titulo": dados.get("Title"),
                    "ano": dados.get("Year"),
                    "nota": dados.get("imdbRating")
                }
            else:
                return {"titulo": nome_da_serie, "erro": "Série não encontrada."}
        
        except Exception:
            return {"erro": "Falha de conexão com o banco de dados de filmes."}

    def listar_favoritas(self):
        """O coração da automação: Loop (Seção V.1.d)"""
        resultados_finais = []
        minha_lista = ["Breaking Bad", "Naruto", "SerieQueNaoExiste"] 
        
        for nome in minha_lista:
            resultado = self.buscar_serie(nome)
            resultados_finais.append(resultado)
            
        return resultados_finais 

from assistente import AssistenteMaratona

def executar_teste_terminal():
    print("Iniciando Assistente de Maratonas...")
    robo = AssistenteMaratona()
    resultados = robo.listar_favoritas()
    for item in resultados:
        print(item)

if __name__ == "__main__":
    executar_teste_terminal()