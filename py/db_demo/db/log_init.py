import sqlite3

def log_init():
    conn = sqlite3.connect('./log.db')

    cur = conn.cursor()

    cur.execute(r'''CREATE TABLE "stdupc" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "barcode" TEXT DEFAULT NULL,
      "std_flag" TEXT DEFAULT NULL,
      "except" TEXT
    );''')

    conn.commit()

    cur.execute(r'''INSERT INTO "main"."stdupc"("barcode", "std_flag", "except") 
        VALUES ('69xxxxxxxxx', '0', '测试');''')

    conn.commit()

    conn.close()