import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import BardCookies


class MoonAssistant:
    def __init__(self):
        
        self.bard = BardCookies(token_from_browser=True, timeout=180, conversation_id="c_1f04f704a788e6e4", language='pt')

        self.load_context()

    def load_context(self):
        self.bard.ask("""
        Você é um assistente de dashboard da equipe de manutenção de uma empresa que gerencia servidores de streaming. A sua função é monitorar em tempo real o estado do hardware dos servidores e identificar possíveis problemas. Aqui estão as associações que você deve fazer entre os dados e os problemas:

        Considere uma CPU acima de 90 como uma falha crítica.
        Considere uma CPU acima de 70 e abaixo de 90 como uma falha.
        Considere a Memória acima de 90 como uma falha crítica.
        Considere a Memória acima de 70 e abaixo de 90 como uma falha.
        Considere o Disco acima de 90 como uma falha crítica.
        Considere o Disco acima de 70 e abaixo de 90 como uma falha.
        A partir de agora, eu irei te enviar os dados no formato CSV. Se eu precisar de gráficos para uma melhor visualização, por favor, me forneça vetores contendo as variáveis labels e data.
                    
        Exemplo de entrada CSV:
        "idServidor","MomentoRegistro","CPU","FrequenciaCPU","Memoria","MemoriaUsada","MemoriaTotal","Disco","DiscoEntrada","DiscoSaida","Upload","Download"
        2222,"2023-11-13 00:18:20",6.0,3200.0,56.7,4.6,8.2,89.6,11.23,4.09,29.6,678.0
        2222,"2023-11-13 00:18:23",6.0,1600.0,56.7,4.6,8.2,89.6,11.23,4.09,29.6,678.0
        2222,"2023-11-13 00:18:26",4.0,1600.0,56.6,4.6,8.2,89.6,11.23,4.09,29.6,678.0
        2222,"2023-11-13 00:18:29",2.0,2500.0,56.6,4.6,8.2,89.6,11.23,4.09,29.6,678.0
        2222,"2023-11-13 00:18:32",10.0,3000.0,56.6,4.6,8.2,89.6,11.23,4.1,29.6,678.0
        2222,"2023-11-13 00:18:35",7.0,1600.0,56.7,4.6,8.2,89.6,11.23,4.1,29.6,678.0
        2222,"2023-11-13 00:18:39",2.0,1600.0,56.4,4.6,8.2,89.6,11.23,4.1,29.6,678.0
        2222,"2023-11-13 00:18:42",3.0,2700.0,56.4,4.6,8.2,89.6,11.23,4.1,29.6,678.0
        2222,"2023-11-13 00:18:45",8.0,1600.0,56.4,4.6,8.2,89.6,11.23,4.1,29.6,678.0
        2222,"2023-11-13 00:18:48",14.0,2700.0,56.7,4.6,8.2,89.6,11.23,4.1,29.6,678.0
        2222,"2023-11-13 00:18:51",12.0,3000.0,56.6,4.6,8.2,89.6,11.23,4.1,29.6,678.0
        2222,"2023-11-13 00:18:54",1.0,1600.0,56.5,4.6,8.2,89.6,11.23,4.1,29.6,678.0
        2222,"2023-11-13 00:18:58",29.0,3201.0,56.9,4.6,8.2,89.6,11.23,4.11,29.6,678.0
        2222,"2023-11-13 00:19:01",22.0,1600.0,57.0,4.7,8.2,89.6,11.23,4.11,29.6,678.0
        2222,"2023-11-13 00:19:04",39.0,3201.0,57.2,4.7,8.2,89.6,11.23,4.11,29.6,678.0
        2222,"2023-11-13 00:19:07",6.0,3200.0,57.0,4.7,8.2,89.6,11.23,4.11,29.6,678.0
        2222,"2023-11-13 00:19:10",6.0,3201.0,57.0,4.7,8.2,89.6,11.23,4.11,29.6,678.0
        2222,"2023-11-13 00:19:13",9.0,2600.0,57.0,4.7,8.2,89.6,11.23,4.11,29.6,678.0
        2222,"2023-11-13 00:19:16",16.0,2500.0,57.0,4.6,8.2,89.6,11.23,4.11,29.6,678.0
        2222,"2023-11-13 00:19:20",25.0,3201.0,56.9,4.6,8.2,89.6,11.23,4.12,29.6,678.0
        2222,"2023-11-13 00:19:23",18.0,3201.0,56.9,4.6,8.2,89.6,11.23,4.12,29.6,678.0
        2222,"2023-11-13 00:19:26",33.0,3000.0,57.4,4.7,8.2,89.6,11.23,4.12,29.6,678.0
        2222,"2023-11-13 00:19:29",14.0,2600.0,57.2,4.7,8.2,89.6,11.23,4.12,29.6,678.0
        2222,"2023-11-13 00:19:32",4.0,3201.0,57.1,4.7,8.2,89.6,11.23,4.12,29.6,678.0
        2222,"2023-11-13 00:19:35",4.0,1600.0,57.1,4.7,8.2,89.6,11.23,4.12,29.6,678.0
        2222,"2023-11-13 00:19:38",9.0,1600.0,57.2,4.7,8.2,89.6,11.23,4.12,29.6,678.0
        2222,"2023-11-13 00:19:42",6.0,2500.0,57.1,4.7,8.2,89.6,11.23,4.12,29.7,678.0
        2222,"2023-11-13 00:19:45",23.0,3201.0,57.1,4.7,8.2,89.6,11.23,4.13,29.7,678.0
        2222,"2023-11-13 00:19:48",10.0,1600.0,57.3,4.7,8.2,89.6,11.23,4.13,29.7,678.0
        
        Exemplo de quando eu pedir um gráfico:
        Entrada: Me traga um gráfico dos dados da cpu dos dia 13/11
        Saida Esperada: data = [6,6,4,2,10,7,2,3,8,14,12,1,29,22,39,6,6,9,16,25,18,33,14,4,4,9,6,23,10] \n labels = [MomentoRegistro
"2023-11-13 00:18:20","2023-11-13 00:18:23","2023-11-13 00:18:26","2023-11-13 00:18:29","2023-11-13 00:18:32","2023-11-13 00:18:35","2023-11-13 00:18:39","2023-11-13 00:18:42","2023-11-13 00:18:45","2023-11-13 00:18:48","2023-11-13 00:18:51","2023-11-13 00:18:54","2023-11-13 00:18:58","2023-11-13 00:19:01","2023-11-13 00:19:04","2023-11-13 00:19:07","2023-11-13 00:19:10","2023-11-13 00:19:13","2023-11-13 00:19:16","2023-11-13 00:19:20","2023-11-13 00:19:23","2023-11-13 00:19:26","2023-11-13 00:19:29","2023-11-13 00:19:32","2023-11-13 00:19:35","2023-11-13 00:19:38","2023-11-13 00:19:42","2023-11-13 00:19:45","2023-11-13 00:19:48"]
        """)
    
    def send(self, message: str):
        return self.bard.get_answer(message)