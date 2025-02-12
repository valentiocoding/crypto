import streamlit as st
import sqlite3
from database import input_data, transaction_data
import datetime


data = transaction_data()

category = st.selectbox(
    "Select a category",
    ["Top Up Toko Crypto", "Buy USDT on Toko Crypto", "Transfer USDT to Binance",
     "Buy Coin on Binance", "Sell Coin on Binance", "Transfer USDT to Toko Crypto", "Sell USDT on Toko Crypto", "Transfer to Bank Account"]
)


if category == "Top Up Toko Crypto":
    total_topup = data[data['keterangan'] == 'Top Up Toko Crypto']['rupiah'].sum()
    col1,col2 = st.columns(2)
    col1.metric("Total Topup", f"{total_topup:,.2f}", border=True)
    col2.metric("Saldo Toko Crypto", f"{data['saldo_toko'].sum():,.2f}", border=True)
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Top Up Toko Crypto"
        date = st.date_input("Date")
        rupiah = st.number_input("Rupiah", format="%.10f")
        saldo = st.number_input("Saldo Toko Crypto", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            
            input_data(date,rupiah,saldo,0,0,0,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Buy USDT on Toko Crypto":
    col1,col2 = st.columns(2)
    col1.metric("Saldo Toko Crypto", f"{data['saldo_toko'].sum():,.2f}", border=True)
    col2.metric("USDT Toko Crypto", f"{data['usdt'].sum():,.2f}", border=True)
    usdt_rate = data[data['keterangan'] == 'Buy USDT on Toko Crypto']['rate'].mean()
    st.metric("Average Buy Rate USDT",f"{usdt_rate:,.2f}", border=True )
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Buy USDT on Toko Crypto"
        date = st.date_input("Date")
        saldo = st.number_input("Saldo Toko Crypto", format="%.10f")
        rate = st.number_input("Rate", format="%.10f")
        usdt = st.number_input("USDT", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            saldo = -1 * saldo
            input_data(date,0,saldo,rate,usdt,0,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Transfer USDT to Binance":
    col1,col2 = st.columns(2)
    col1.metric("USDT Toko Crypto", f"{data['usdt'].sum():,.2f}", border=True)
    col2.metric("USDT Binance", f"{data['usdt_binance'].sum():,.2f}", border=True)
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Transfer USDT to Binance"
        date = st.date_input("Date")
        usdt = st.number_input("USDT", format="%.10f")
        usdt_binance = st.number_input("USDT Binance", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            usdt = -1 * usdt
            input_data(date,0,0,0,usdt,usdt_binance,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Buy Coin on Binance":
    coin_list = data[data['coin'] != ""]
    coin_list = coin_list['coin'].unique()
    with st.expander("See Avg Buy Rate Coin"):
        coin = st.selectbox(
            "Select Coin",
            coin_list
        )
        average_coin_rate = data[(data['coin'] == coin) & (data['keterangan'] == 'Buy Coin on Binance')]['rate'].mean()
        
        st.metric("Average Buy Rate Coin", f"{average_coin_rate:,.2f}", border=True)


    with st.form("my_form", clear_on_submit=True):
        date = st.date_input("Date")
        coin = st.text_input("Coin")
        rate = st.number_input("Rate", format="%.10f")
        selectedcategory = "Buy Coin on Binance"
        usdt_binance = st.number_input("USDT Binance", format="%.10f")
        QtyCoin = st.number_input("QtyCoin", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            usdt_binance = -1 * usdt_binance
            input_data(date,0,0,rate , 0, usdt_binance, coin, QtyCoin, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Sell Coin on Binance":

    with st.expander("See Avg Sell Rate Coin"):
        coin_list = data[data['coin'] != ""]
        coin_list = coin_list['coin'].unique()
        coin = st.selectbox(
            "Select Coin",
            coin_list
        )

        average_coin_rate = data[(data['coin'] == coin) & (data['keterangan'] == 'Sell Coin on Binance')]['rate'].mean()
        
        st.metric("Average Sell Rate Coin", f"{average_coin_rate:,.2f}", border=True)

    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Sell Coin on Binance"
        date = st.date_input("Date")
        coin = st.text_input("Coin")
        QtyCoin = st.number_input("QtyCoin", format="%.10f")
        rate = st.number_input("Rate", format="%.10f")
        usdt_binance = st.number_input("USDT Binance", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            QtyCoin = -1 * QtyCoin
            input_data(date,0,0,rate , 0, usdt_binance, coin, QtyCoin, selectedcategory)
            st.success("Berhasil input.")
            
            
            
elif category == "Transfer USDT to Toko Crypto":
    col1,col2 = st.columns(2)

    col1.metric("USDT Binance", f"{data['usdt_binance'].sum():,.2f}", border=True)
    col2.metric("USDT Toko Crypto", f"{data['usdt'].sum():,.2f}", border=True)
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Transfer USDT to Toko Crypto"
        date = st.date_input("Date")
        usdt_binance = st.number_input("USDT on Binance", format="%.10f")
        usdt = st.number_input("USDT Toko Crypto", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            usdt_binance = -1 * usdt_binance
            input_data(date,0,0,0,usdt,usdt_binance,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Sell USDT on Toko Crypto":
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Sell USDT on Toko Crypto"
        date = st.date_input("Date")
        rate = st.number_input("Rate", format="%.10f")
        usdt = st.number_input("USDT", format="%.10f")
        saldo = st.number_input("Saldo Toko Crypto", format="%.10f")

        button = st.form_submit_button("Submit")
        
        if button:
            usdt = -1 * usdt
            input_data(date,0,saldo,rate,usdt,0,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Transfer to Bank Account":
    col1,col2 = st.columns(2)

    col1.metric("Saldo Toko Crypto", f"{data['saldo_toko'].sum():,.2f}", border=True)
    col2.metric("Rupiah", f"{data['rupiah'].sum():,.2f}", border=True)
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Transfer to Bank Account"
        date = st.date_input("Date")
        saldo = st.number_input("Saldo Toko Crypto", format="%.10f")
        rupiah = st.number_input("Rupiah", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            saldo = -1 * saldo
            input_data(date,rupiah,saldo,0,0,0,"",0, selectedcategory)
            st.success("Berhasil input.")
            