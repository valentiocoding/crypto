import streamlit as st
import sqlite3
from database import input_data
import datetime


st.write("hey")

category = st.selectbox(
    "Select a category",
    ["Top Up Toko Crypto", "Buy USDT on Toko Crypto", "Transfer USDT to Binance",
     "Buy Coin on Binance", "Sell Coin on Binance", "Transfer USDT to Toko Crypto", "Sell USDT on Toko Crypto", "Transfer to Bank Account"]
)


if category == "Top Up Toko Crypto":
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Top Up Toko Crypto"
        rupiah = st.number_input("Rupiah", format="%.10f")
        saldo = st.number_input("Saldo Toko Crypto", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            date = datetime.datetime.now()
            
            input_data(date,rupiah,saldo,0,0,0,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Buy USDT on Toko Crypto":
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Buy USDT on Toko Crypto"
        saldo = st.number_input("Saldo Toko Crypto", format="%.10f")
        rate = st.number_input("Rate", format="%.10f")
        usdt = st.number_input("USDT", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            date = datetime.datetime.now()
            saldo = -1 * saldo
            input_data(date,0,saldo,rate,usdt,0,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Transfer USDT to Binance":
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Transfer USDT to Binance"
        usdt = st.number_input("USDT", format="%.10f")
        usdt_binance = st.number_input("USDT Binance", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            date = datetime.datetime.now()
            usdt = -1 * usdt
            input_data(date,0,0,0,usdt,usdt_binance,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Buy Coin on Binance":
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Buy Coin on Binance"
        usdt_binance = st.number_input("USDT Binance", format="%.10f")
        rate = st.number_input("Rate", format="%.10f")
        coin = st.text_input("Coin")
        QtyCoin = st.number_input("QtyCoin", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            date = datetime.datetime.now()
            usdt_binance = -1 * usdt_binance
            input_data(date,0,0,rate , 0, usdt_binance, coin, QtyCoin, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Sell Coin on Binance":
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Sell Coin on Binance"
        usdt_binance = st.number_input("USDT Binance", format="%.10f")
        rate = st.number_input("Rate", format="%.10f")
        coin = st.text_input("Coin")
        QtyCoin = st.number_input("QtyCoin", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            date = datetime.datetime.now()
            QtyCoin = -1 * QtyCoin
            input_data(date,0,0,rate , 0, usdt_binance, coin, QtyCoin, selectedcategory)
            st.success("Berhasil input.")
            
            
            
elif category == "Transfer USDT to Toko Crypto":
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Transfer USDT to Toko Crypto"
        usdt_binance = st.number_input("USDT on Binance", format="%.10f")
        usdt = st.number_input("USDT Toko Crypto", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            date = datetime.datetime.now()
            usdt_binance = -1 * usdt_binance
            input_data(date,0,0,0,usdt,usdt_binance,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Sell USDT on Toko Crypto":
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Sell USDT on Toko Crypto"
        rate = st.number_input("Rate", format="%.10f")
        usdt = st.number_input("USDT", format="%.10f")
        saldo = st.number_input("Saldo Toko Crypto", format="%.10f")

        button = st.form_submit_button("Submit")
        
        if button:
            date = datetime.datetime.now()
            usdt = -1 * usdt
            input_data(date,0,saldo,rate,usdt,0,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Transfer to Bank Account":
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Transfer to Bank Account"
        saldo = st.number_input("Saldo Toko Crypto", format="%.10f")
        rupiah = st.number_input("Rupiah", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            date = datetime.datetime.now()
            saldo = -1 * saldo
            input_data(date,rupiah,saldo,0,0,0,"",0, selectedcategory)
            st.success("Berhasil input.")
            