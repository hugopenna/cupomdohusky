import sqlite3


con = sqlite3.connect("main.db")
cur = con.cursor()
cur.execute("""CREATE TABLE cupons(
    cupom_id, 
    given_date DEFAULT NULL, 
    given_by DEFAULT NULL, 
    taken_date DEFAULT NULL, 
    taken_by DEFAULT NULL
    )""")

