import sqlite3


con = sqlite3.connect("main.db")
cur = con.cursor()
cur.execute("""CREATE TABLE cupons (
    cupom_id TEXT NOT NULL,
    given_by TEXT DEFAULT NULL,
    given_date TEXT DEFAULT NULL,
    taken_by TEXT DEFAULT NULL,
    taken_date TEXT DEFAULT NULL
    );""")

cur.execute("""INSERT INTO cupons VALUES 
(cupom_id='236F06462E95', given_by='Hugopenna')
""")