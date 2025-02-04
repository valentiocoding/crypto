import sqlite3
import io
import pandas as pd
import streamlit as st
from database import transaction_data








data = transaction_data()

st.title("Dashboard")
st.divider()

col1, col2 = st.columns(2)
total_topup = data[data['keterangan'] == 'Top Up Toko Crypto']['rupiah'].sum()
col1.metric(label="Total Topup", value=f"Rp {total_topup:,.0f}", border=True)
col2.metric(label="Saldo Toko Crypto", value=f"{data['saldo_toko'].sum():,.2f}", border=True)





usdt = data['usdt'].sum()
col1.metric("USDT Toko Crypto", f"{usdt:,.2f}", border=True)

usdt_rate = data[data['keterangan'] == 'Buy USDT on Toko Crypto']['rate'].mean()
col2.metric("Average USDT Buy Rate", f"{usdt_rate:,.2f}", border=True)


st.divider()
st.header("Binance")
usdt_binance = data['usdt_binance'].sum()
col1,col2 = st.columns(2)
st.metric("USDT Binance",f"{usdt_binance:,.2f}", border=True)



grouped_coin = data.groupby('coin')['QtyCoin'].sum().reset_index()
grouped_coin = grouped_coin[grouped_coin['coin'] != ""]

st.subheader("Coin List")
st.dataframe(grouped_coin)


with st.expander("Purchase Coin History") :
    history = data[data['keterangan'] == 'Buy Coin on Binance']
    history = history[['date', 'coin', 'QtyCoin', 'rate']]
    history.rename(columns={'rate': 'rate(usdt)'}, inplace=True)
    st.dataframe(history)








# Membuat objek BytesIO untuk menyimpan file Excel dalam memori
excel_data = io.BytesIO()

# Menulis DataFrame ke dalam objek BytesIO
data.to_excel(excel_data, index=False)

# Mengembalikan pointer ke awal file untuk dibaca
excel_data.seek(0)

# Tombol unduh
st.download_button(
    label="Download Excel",
    data=excel_data,
    file_name="transactions.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)