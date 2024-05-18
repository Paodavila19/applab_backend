import functools
import db
import pymysql

def get_users():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM users"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_user(user_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM users WHERE id = {}".format(user_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_user(name, lastname):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO users(name, lastname) VALUES('{}','{}')".format(name, lastname)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_user(name, lastname, user_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE users set name='{0}', lastname='{1}' WHERE id = {2}".format(name, lastname, user_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_user(user_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM users WHERE id = {}".format(user_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
