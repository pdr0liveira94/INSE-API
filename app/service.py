from app import app
from config import mysql

def get_enterprise_id_by_name(name):
    try:
        parsedName = name.replace('_', ' ')
        print(parsedName)
        cursor = mysql.connection.cursor()
        cursor.execute("""
            select id from empresa 
            where nomefantasia like '""" + parsedName + "%'")
        result = cursor.fetchone()

        cursor.close()
        return str(result[0])
    except Exception as e:
        print(e)

def get_enterprise_by_id(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT i.dimensao, i.impacto 
            FROM empresa AS e
            JOIN plano_estrategico AS pe
            ON pe.empresa = e.id
            JOIN impacto AS i
            ON i.plano_estrategico = pe.id
            WHERE pe.ativo = 1
            AND i.perspectiva_bsc = 'Geral'
            AND e.id = '""" + id + "'")

        queryresult = cursor.fetchall()

        cursor.execute(
            """
                SELECT nomefantasia
                FROM empresa
                WHERE id = '""" + id + "'")
        
        name = cursor.fetchone()
        print(queryresult)
        cursor.close()
        
        result = {
            "name": ''.join(name),
            "rankings": dict((str(dimension), str(float(impact/100))) for dimension, impact in queryresult)
        }

        return result
    except Exception as e:
        print(e)

def get_enterprises():
    cursor = mysql.connection.cursor()
    cursor.execute(
        """
            SELECT nomefantasia
            FROM empresa;
        """
    )

    result = cursor.fetchall()
    cursor.close()
    return [''.join(name) for name in result]