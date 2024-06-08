import functools
import db
import pymysql

def get_pacientes():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM pacientes"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_paciente(paciente_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM pacientes WHERE id_paciente = {}".format(paciente_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_paciente(tipo_id, nombre, email, tipo_sangre, genero, edad, fecha_nacimiento, dir, celular, eps):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO pacientes(tipo_id, nombre, email, tipo_sangre, genero, edad, fecha_nacimiento, dir, celular, eps) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(tipo_id, nombre, email, tipo_sangre, genero, edad, fecha_nacimiento, dir, celular, eps)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK paciente creado", "id": id_org}
    finally:
        con.close()

def update_paciente(tipo_id, nombre, email, tipo_sangre, genero, edad, fecha_nacimiento, dir, celular, eps, paciente_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE pacientes set tipo_id='{0}', nombre='{1}',email='{2}',tipo_sangre='{3}',genero='{4}',edad='{5}',fecha_nacimiento='{6}',dir='{7}',celular='{8}',eps='{9}' WHERE id_paciente = {10}".format(tipo_id, nombre, email, tipo_sangre, genero, edad, fecha_nacimiento, dir, celular, eps, paciente_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK, paciente actualizado"}
    finally:
        con.close()

def delete_paciente(paciente_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM pacientes WHERE id_paciente = {}".format(paciente_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK, paciente aniquilado"}
    finally:
        con.close()



