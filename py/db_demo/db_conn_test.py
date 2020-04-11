import db

org_db_info = {
    "host": '192.168.10.1\\***',
    "user": "sa",
    "database": "demo_project",
    "password": "******"
}

with db.conn.log() as log, db.conn.org(org_db_info) as org:
    qs = log.execute(r'''select * from "main"."stdupc"''')
    print(list(qs))
    qs = org.execute(r'''select top 1 * from orgdoc''')
    print(list(qs))

input()