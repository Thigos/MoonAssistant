import mysql.connector
import pyodbc
import json

class DBConnection:
    def __init__(self):
        self.__connectionMysql = mysql.connector.connect(
            host='localhost',
            database='streamoon',
            user='StreamoonUser',
            password='Moon2023'
        )

        self.__connectionSQLServer = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=18.208.1.120;'
            'DATABASE=streamoon;'
            'UID=StreamoonUser;'
            'PWD=Moon2023;'
            'TrustServerCertificate=yes;'
        )

    def writeDB(self, dictData : dict, idUsuario: int, isBot: bool):
        jsonstr = json.dumps(dictData, ensure_ascii=False)
        instrucao = f"INSERT INTO logMoonAssistant (fkUsuario, msg, isBot) VALUES ({idUsuario}, '{jsonstr}', {int(isBot)});"

        #SQL Server Insety
        cursor = self.__connectionSQLServer.cursor()
        cursor.execute(instrucao)
        self.__connectionSQLServer.commit()
        cursor.close()

        #Mysql Insert
        cursor = self.__connectionMysql.cursor()
        cursor.execute(instrucao)

        self.__connectionMysql.commit()
        cursor.close()

