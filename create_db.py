import sqlite3


con = sqlite3.connect("main.db")
cur = con.cursor()
cur.execute("CREATE TABLE cupons(cupom_id, given_date, given_by, taken_date, taken_by)")

