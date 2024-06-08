import functools
import db
import pymysql

def get_registros():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM registros"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_registro(registro_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM registros WHERE id_registro = {}".format(registro_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_resgistro(id_paciente, personal, cargo, prueba, valor_resultado, unidad_resultado):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO registros(id_paciente, personal, cargo, prueba, valor_resultado, unidad_resultado) VALUES('{}','{}','{}','{}','{}','{}')".format(id_paciente, personal, cargo, prueba, valor_resultado, unidad_resultado)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK, registro creado", "id": id_org}
    finally:
        con.close()

def update_registro(id_paciente, personal, cargo, prueba, valor_resultado, unidad_resultado, registro_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE registros set id_paciente='{0}', personal='{1}',cargo='{2}',prueba='{3}',valor_resultado='{4}',unidad_resultado='{5}' WHERE id_registro = {6}".format(id_paciente, personal, cargo, prueba, valor_resultado, unidad_resultado, registro_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK, registro actualizado"}
    finally:
        con.close()

def delete_registro(registro_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM registros WHERE id_registro = {}".format(registro_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK, registro aniquilado"}
    finally:
        con.close()