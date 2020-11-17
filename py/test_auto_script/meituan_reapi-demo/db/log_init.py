import sqlite3

def log_init():
    conn = sqlite3.connect('./log.db')

    cur = conn.cursor()

    cur.execute(r'''CREATE TABLE "batchsave" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "time" TEXT DEFAULT NULL,
      "app_medicine_code" TEXT DEFAULT NULL,
      "error_msg" TEXT DEFAULT NULL
    );''')


    conn.close()