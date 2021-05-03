import sqlite3
conn = sqlite3.connect('jarvis_binance.db')
conn.execute("UPDATE BINANCE_STATUS set status = 'RUNNING' where user = 'courtney'")
conn.execute("INSERT INTO BINANCE_POSITIONS(user,exchange, symbol, entry_time_utc, price, side, open_pos,dollar_qty) VALUES('courtney','test', 'test', 'test', 'test', 'test', 'test','test')")

conn.commit()
conn.close()