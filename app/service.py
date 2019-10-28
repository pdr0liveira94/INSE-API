from flask_mysqldb import MySQL
from app import app

# Database settings
app.config["MYSQL_HOST"] = "localhost" # IP Address
app.config["MYSQL_USER"] = "root" # DB User
app.config["MYSQL_PASSWORD"] = "" # User Password
app.config["MYSQL_DB"] = "inse" # DB Name
mysql = MySQL(app)

def get_enterprises():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        
        # Save changes
        mysql.connection.commit()

        cursor.close()
        return result
    except Exception as e:
        # Revert changes
        mysql.connection.rollback()
        if (mysql.connection not None)
            mysql.connection.close()
        print e

def owns_PEE(strategicPLan):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM plano_estrategico WHERE plano_estrategico = '" + strategicPLan + "'")
        result = cursor.fetchall()
        cursor.close()
        return result.rowcount
    except:
        cursor.close()
        return 0

def owns_goals(strategicPlan):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM objetivo WHERE plano_estrategico = '" + strategicPlan + "'")
    result = cursor.fetchall()
    cursor.close()
    return result.rowcount

def owns_values(strategicPlan):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM valor WHERE plano_estrategico = '" + strategicPlan + "'")
    result = cursor.fetchall()
    cursor.close()
    return result.rowcount

def CNPJ_exists(cnpj):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM empresa WHERE cnpj = '" + cnpj + "'")
    result = cursor.fetchall()
    cursor.close()
    return result.rowcount

def email_exists(email):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuario WHERE email = '" + email + "'")
    result = cursor.fetchall()
    cursor.close()
    return result.rowcount


def valid_login(email, pwd):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuario WHERE email = '" + email + "'")
    result = cursor.fetchone()
    if (result.rowcount > 0 and pwd == result['senha']):
        cursor.execute("SELECT * FROM empresa WHERE id = '" + result['id'] + "'")
        user = cursor.fetchone()
        if (user.rowcount > 0):
            returnValue = 1
        else:
            returnValue = 0
    else:
        returnValue = 0
    
    cursor.close()
    return result