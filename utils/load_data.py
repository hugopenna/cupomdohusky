import sqlite3

cupons = ['0A13A68C0291', 'DFAA143C409F', '2F95F410E869', '236F06462E95', 'D4D79B0593A3', 'E2A7204D0605', 'FFC0A68DC165']

con = sqlite3.connect('main.db')
cur = con.cursor()

for cupon in cupons:
    cur.execute("INSERT INTO cupons (cupom_id) VALUES (?);", (cupon,))
    con.commit()
