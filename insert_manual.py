import mysql.connector as mariadb

#conecta base de datos
conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306
    )

#crea cursor
cur = conn.cursor()

#recibe respuesta
url = input("Introduzca url: ")
texto = input("Introduzca título: ")

respuesta= (url,texto)

sql= "Insert into web_scrapping(url, title) values(?,?)"

#inserta datos a la tabla
if (cur.execute(sql,respuesta)):
    print("Ingresado con exito")
else: print("Ha ocurrido un error")


cur.commint()
cur.close()
