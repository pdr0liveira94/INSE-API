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
    result = {}

    try:
        cursor = mysql.connection.cursor()

        # fetch enterprise's indexes
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

        dimensions = cursor.fetchall()
        result['indexes'] = dict((str(dimension), str(float(impact))) for dimension, impact in dimensions)
        print(result)
        
        # fetch enterprise's name
        cursor.execute(
            """
                SELECT nomefantasia
                FROM empresa
                WHERE id = '""" + id + "'")
        
        name = cursor.fetchone()
        print(name)
        result['name'] = ''.join(name)

        # # TODO
        # # fetch enterprise's rankings
        # cursor.execute(
        #     """
        #         SELECT i.dimensao, i.impacto 
        #         FROM empresa AS e
        #         JOIN plano_estrategico AS pe
        #         ON pe.empresa = e.id
        #         JOIN impacto AS i
        #         ON i.plano_estrategico = pe.id
        #         WHERE pe.ativo = 1
        #         AND i.perspectiva_bsc = 'Geral'
        #         AND e.id = '""" + id + "'"
        # )

        cursor.close()

        return result
    except Exception as e:
        print(e)

def get_enterprises(branch, state, city):
    suffix = ""
    print(branch, state, city)

    cursor = mysql.connection.cursor()
    sql = """
            SELECT nomefantasia
            FROM empresa as emp
        """

    if branch is not None:
        sql = sql + """
                JOIN ramo_atuacao as ra
                ON ra.id = emp.ramo
            """
        suffix = """
            AND ra.ramo = '""" + branch + """'
        """

    if state is not None:
        sql = sql + """
                JOIN endereco as end
                ON end.id = emp.endereco
                WHERE end.estado = '""" + state + """'
            """
    if city is not None:
        sql = sql + """
                AND end.cidade = '""" + city + """'
            """
    
    sql = sql + suffix
    print(sql)

    cursor.execute(sql)
    result = cursor.fetchall()
    names = [''.join(name) for name in result]
    cursor.close()
    return names

def get_branches():
    try:
        cursor = mysql.connection.cursor()
        sql = """
                SELECT atividade
                FROM ramo_atuacao
            """

        cursor.execute(sql)
        result = cursor.fetchall()
        names = [''.join(name) for name in result]
        cursor.close()
        names.sort()
        return names
    except Exception as e:
        print(e)
