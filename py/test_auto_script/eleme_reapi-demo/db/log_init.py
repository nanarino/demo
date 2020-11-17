import sqlite3

def log_init():
    conn = sqlite3.connect('./log.db')

    cur = conn.cursor()

    cur.execute(r'''CREATE TABLE "stdupc" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "time" TEXT DEFAULT NULL,
      "barcode" TEXT DEFAULT NULL,
      "std_flag" TEXT DEFAULT NULL,
      "except" TEXT
    );''')
    cur.execute(r'''CREATE TABLE "skuMap" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "time" TEXT DEFAULT NULL,
      "goodscode" TEXT DEFAULT NULL,
      "errno" integer DEFAULT 0,
      "error" TEXT
    );''')
    cur.execute(r'''CREATE TABLE "catMap" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "time" TEXT DEFAULT NULL,
      "goodscode" TEXT DEFAULT NULL,
      "errno" integer DEFAULT 0,
      "error" TEXT
    );''')
    cur.execute(r'''CREATE TABLE "syncFailed" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "time" TEXT DEFAULT NULL,
      "shop_id" TEXT DEFAULT NULL,
      "goodscode" TEXT DEFAULT NULL,
      "errno" integer DEFAULT 0,
      "error" TEXT
    );''')
    conn.commit()

    conn.close()