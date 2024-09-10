import sqlite3 as sql

con = sql.connect('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS livro')

sql = '''CREATE TABLE "livro" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "TITULO" TEXT,
    "AUTOR" TEXT,
    "ANO" TEXT     
    )'''
cur.execute(sql)
con.commit()
con.close()