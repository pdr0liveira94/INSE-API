from flask_mysqldb import MySQL
from app import app

# Database settings
app.config['MYSQL_HOST'] = '<IP Address>' # Put your IP Address
app.config['MYSQL_USER'] = '<DB User>' # Put your DB User
app.config['MYSQL_PASSWORD'] = '<User Password>' # Put your User Password
app.config['MYSQL_DB'] = '<DB Name>' # Put your DB Name
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
        if(mysql.connection not None)
            mysql.connection.close()
        print e
