import db

log = db.conn.log()

qs = log.execute(r'''select * from "main"."stdupc"''')

print(list(qs))

log.close()

org = db.conn.org({
    "host": '192.168.10.1\\cbp',
    "user": "sa",
    "database": "race",
    "password": "xf67680"
})

qs = org.execute(r'''select top 1 * from orgdoc''')

print(list(qs))

org.close()

input()