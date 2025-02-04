import streamlit as st
from database import transaction_data
import pandas as pd








data = transaction_data()

selectcoin = data[data['coin'] != ""]
selectcoin = st.selectbox("Select Coin", selectcoin['coin'].unique())

average_coin_rate = data[(data['coin'] == selectcoin) & (data['keterangan'] == 'Buy Coin on Binance')]['rate'].mean()


st.header("Estimate Profit Tools")
col1,col2 = st.columns(2)
col1.metric(f"Average {selectcoin} Buy Rate", f"{average_coin_rate:,.2f}", border=True)
usdt_rate_buy = data[data['keterangan'] == 'Buy USDT on Toko Crypto']['rate'].mean()
col2.metric(f"Average USDT Buy Rate", f"{usdt_rate_buy:,.2f}", border=True)


coin_total = data[data['coin'] == selectcoin]['QtyCoin'].sum()

st.metric(f"My {selectcoin} Coin", f"{coin_total:,.2f}")

qty_coin = st.number_input("Masukkan Qty BTC", format="%.10f", help="Estimasi Jumlah Coin untuk dijual")

if qty_coin > coin_total:
    st.warning("You do not have enough coins to sell.")
    st.stop()


col1,col2 = st.columns(2)
harga_btc_now = col1.number_input("Masukkan Harga BTC Sekarang", format="%.10f")
usdt_rate = col2.number_input("Masukkan Rate USDT Sekarang", format="%.10f")



if harga_btc_now and usdt_rate and qty_coin:

    modal = qty_coin * average_coin_rate * usdt_rate_buy

    st.write(f"Modal: {modal:,.2f}")

    profit = qty_coin * harga_btc_now * usdt_rate
    st.write(f"Total Jual: {profit:,.2f}")

    estimasi_profit = profit - modal
    st.write(f"Estimasi Profit: {estimasi_profit:,.2f}")






# Menambahkan styling menggunakan st.markdown
        # styled_table = df.style.apply(lambda x: ['background-color: #000080' if x.name == len(df)-1 else '' for i in x], axis=1)
        # st.dataframe(styled_table)