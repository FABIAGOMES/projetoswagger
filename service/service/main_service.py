import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import string
class PalindromeService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):
        """"
        Carrega o servico
        """

        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)
        start_time = time.time()

        response_predicts = self.palindrome(texts['textoMensagem'])

        logger.debug(mensagens.FIM_SERVICO)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['textoMensagem'])
        df_response['predict'] = response_predicts

        df_response = df_response.drop(columns=['textoMensagem'])

        response = {
            "listaClassificacoes": json.loads(df_response.to_json(
                orient='records', force_ascii=False))}

        return response

    def palindrome(self, texts):
        respostas = []

        for text in texts:

            text=text.replace(" ","")
            if text == text[::-1]:
                respostas.append("palindrome")
            else:
                respostas.append("nao palindrome")
        return respostas
