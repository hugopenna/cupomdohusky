import sqlite3


con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("""CREATE TABLE cupons (
    cupom_id TEXT NOT NULL,
    given_by TEXT DEFAULT NULL,
    given_date TEXT DEFAULT NULL,
    taken_by TEXT DEFAULT NULL,
    taken_date TEXT DEFAULT NULL
    );""")