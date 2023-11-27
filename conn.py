import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentokentat',
         user='root',
         password='password',
         autocommit=True
         )

def haeMaakoodi(maak):
    sql = "SELECT name, iso_region, type FROM airport "
    sql += " WHERE ident = '" + maak + "' "
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for i in tulos:
            print(i)
    return


maak = input("Anna ICAO: ")
haeMaakoodi(maak)