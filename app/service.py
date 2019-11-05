from app import app
from config import mysql

def get_enterprise_id_by_name(name):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            select id from empresa 
            where nomefantasia like '""" + name + "%'")
        result = cursor.fetchone()

        cursor.close()
        return result[0]
    except Exception as e:
        print(e)

def get_enterprise_by_id(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT i.perspectiva_bsc, i.impacto 
            FROM empresa AS e
            JOIN plano_estrategico AS pe
            ON pe.empresa = e.id
            JOIN impacto AS i
            ON i.plano_estrategico = pe.id
            WHERE pe.ativo = 1
            AND i.dimensao = 'Geral'
            AND e.id = '""" + id + "'")

        result = cursor.fetchall()
        print(result)
        
        cursor.close()
        return dict((str(dimension), int(impact)) for dimension, impact in result)
    except Exception as e:
        print(e)