import sqlite3
import pandas as pd
# Koneksi ke database SQLite
conn = sqlite3.connect('crypto.db')
c = conn.cursor()


# Membuat tabel topup jika belum ada
c.execute('''
CREATE TABLE IF NOT EXISTS db_transaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATETIME,
    rupiah DECIMAL(20,10),
    saldo_toko DECIMAL(20,10),
    rate DECIMAL(20,10),
    usdt DECIMAL(20,10),
    usdt_binance DECIMAL(20,10),
    coin TEXT,
    QtyCoin DECIMAL(20,10),
    keterangan TEXT
)
''')
    
conn.commit()
conn.close()

def transaction_data():
    conn = sqlite3.connect('crypto.db')  # Hubungkan ke database
    query = "SELECT * FROM db_transaction"  # Ganti dengan query yang sesuai
    df = pd.read_sql(query, conn)  # Membaca data dari query ke DataFrame
    conn.close()  # Menutup koneksi
    return df



def input_data(date,rupiah, saldo_toko, rate, usdt, usdt_binance, coin, QtyCoin, keterangan):
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()
    
    c.execute("""
              
              INSERT INTO db_transaction(date, rupiah, saldo_toko, rate, usdt, usdt_binance, coin, QtyCoin, keterangan)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
              """,
              (date,rupiah, saldo_toko, rate, usdt, usdt_binance, coin, QtyCoin, keterangan)
              )
    conn.commit()
    conn.close()