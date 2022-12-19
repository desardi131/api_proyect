import pandas as pd
import pymysql
# model = pickle.load(open('iri.pkl', 'rb'))

def acceso(dias):

    username = "DataScienceTB22"
    password = "pyquirrinds"
    host = "database-1.ceaq9kvyuwau.us-east-2.rds.amazonaws.com"
    port = "3306"
    cursorclass = pymysql.cursors.DictCursor

    # gets the credentials from .aws/credentials
    db = pymysql.connect(host=host,
                         user=username,
                         password=password,
                         cursorclass=cursorclass,
                         )

    cursor = db.cursor()

    cursor.connection.commit()
    use_db = ''' USE users_web'''
    cursor.execute(use_db)

    sql = '''SELECT * FROM users'''
    cursor.execute(sql)
    tabla = cursor.fetchall()

    #por si quiero que devuelva los últimos 30 o el df entero
    if dias == 'todo':
        tabla = pd.DataFrame(tabla)
    elif dias == 'mes':
        tabla = pd.DataFrame(tabla)
        tabla = tabla[-30:]
    db.close()
    tabla.to_csv('src\static\data\last_30_days.csv')
    return tabla

#acceso()