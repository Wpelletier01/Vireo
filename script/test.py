import mariadb


PORT_FOWARDING = 5533
HOST_OUTSIDE = "127.0.0.1"


DB_USER = "admin"
PASSWORD = "vireo"
DB_NAME = "vireodb"

conn = mariadb.connect(
    
                    user=DB_USER,
                    password=PASSWORD,
                    host=HOST_OUTSIDE,
                    port=PORT_FOWARDING,
                    database=DB_NAME     
                    )                 
cur = conn.cursor()


cur.execute("""

    SELECT Username
                FROM Channels
                WHERE Username = 'wpelletier';

    """)

cid = cur.fetchall()[0][0]
print(cid)

