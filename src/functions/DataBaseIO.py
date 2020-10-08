import sqlite3

def len_Database(db_name,table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    SQL = '''SELECT count(*) FROM "%s";'''%(table_name)
    cursor.execute(SQL)
    l=0
    for x in cursor:
        l=x[0]
    conn.close()
    return l

def read_Database(db_name,table_name,number,column_name):
    conn=sqlite3.connect(db_name)
    cursor=conn.cursor()
    SQL='''SELECT "%s" FROM "%s" WHERE NUMBER="%d";'''%(column_name,table_name,number)
    cursor.execute(SQL)
    data=[]
    for x in cursor:
        data.append(x)
    conn.close()
    return data[0][0]

def update_Database(db_name,table_name,number,column_name,new_value):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    if isinstance(new_value,bool) or isinstance(new_value,int):
        SQL = '''UPDATE "%s" SET "%s"="%d" WHERE NUMBER="%d";''' % (table_name,column_name,  new_value,number)
    elif isinstance(new_value,float):
        SQL = '''UPDATE "%s" SET "%s"="%f" WHERE NUMBER="%d";''' % (table_name,column_name,  new_value,number)
    elif isinstance(new_value,str):
        SQL = '''UPDATE "%s" SET "%s"="%s" WHERE NUMBER="%d";''' % (table_name,column_name,  new_value,number)
    cursor.execute(SQL)
    conn.commit()
    conn.close()