import mysql.connector
from mysql.connector import cursor

def sql_connection():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="",
                                 database="db_idha")
    return db

def input_data(uuid,suhu,detak_jtg,saturasi,ruangan,status):
    db = sql_connection()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO `monitor`(`uuid_pasien`, `waktu_tgl`, `suhu`, `detak_jtg`, `saturasi`, `ruangan`, `status`) VALUES (%s,now(),%s,%s,%s,%s,%s)",(uuid,suhu,detak_jtg,saturasi,ruangan,status))
        db.commit()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)

def cek_data(uuid):
    db = sql_connection()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `uuid_pasien` FROM `monitor` WHERE `uuid_pasien`=%s",(uuid,))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c==None:
        return False
    else:
        return True

def update_data(suhu,detak_jtg,saturasi,ruangan,status,uuid):
    db = sql_connection()
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE `monitor` SET `waktu_tgl`=now(),`suhu`=%s,`detak_jtg`=%s,`saturasi`=%s,`ruangan`=%s,`status`=%s WHERE `uuid_pasien`=%s",(suhu,detak_jtg,saturasi,ruangan,status,uuid))
        db.commit()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)

def cek_ruangan(uuid,ruangan):
    db = sql_connection()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `uuid_pasien` FROM `ruangan` WHERE `uuid_pasien`=%s AND `ruangan`= %s",(uuid,ruangan))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c==None:
        return False
    else:
        return True
    