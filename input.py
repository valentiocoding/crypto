import streamlit as st
import datetime
from google.oauth2 import service_account
from database import input_data, get_data
import gspread
import pandas as pd


st.session_state.data = get_data()

if "data" not in st.session_state:
    st.session_state.data = get_data()
    
data = st.session_state.data




category = st.selectbox(
    "Select a category",
    ["Top Up Toko Crypto","Buy USDT",
     "Buy Coin on Binance", "Sell Coin on Binance"]
)


if category == "Top Up Toko Crypto":
    total_topup = data[data['keterangan'] == 'Top Up Toko Crypto']['rupiah'].sum()
    st.metric("Total Topup", f"{total_topup:,.2f}", border=True)
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Top Up Toko Crypto"
        date = st.date_input("Date", format="DD/MM/YYYY")
        rupiah = st.number_input("Rupiah", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
          
            input_data(date,rupiah,0,0,"",0, selectedcategory)
            st.session_state.data = get_data()
            st.success("Berhasil input.")
            
            
    





elif category == "Buy USDT":
    col1,col2 = st.columns(2)
    usdt_rate = data[data['keterangan'] == 'Buy USDT on Toko Crypto']['rate'].mean()
    st.metric("Average Buy Rate USDT",f"{usdt_rate:,.2f}", border=True )
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Buy USDT on Toko Crypto"
        date = st.date_input("Date")
        rate = st.number_input("Rate", format="%.10f")
        usdt = st.number_input("USDT", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            input_data(date,0,rate,usdt,"",0, selectedcategory)
            st.success("Berhasil input.")
            
            
elif category == "Transfer USDT to Binance":
    col1,col2 = st.columns(2)
    col1.metric("USDT Toko Crypto", f"{data['usdt'].sum():,.2f}", border=True)
    col2.metric("USDT Binance", f"{data['usdt_binance'].sum():,.2f}", border=True)
    with st.form("my_form", clear_on_submit=True):
        selectedcategory = "Transfer USDT to Binance"
        date = st.date_input("Date")
        usdt = st.number_input("USDT", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            usdt = -1 * usdt
            input_data(date,0,0,usdt,"",0, selectedcategory)
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
        date = st.date_input("Date", format="DD/MM/YYYY")
        coin = st.text_input("Coin")
        rate = st.number_input("Rate", format="%.10f")
        selectedcategory = "Buy Coin on Binance"
        QtyCoin = st.number_input("QtyCoin", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            input_data(date,0,rate , 0, coin, QtyCoin, selectedcategory)
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
        date = st.date_input("Date", format="DD/MM/YYYY")
        coin = st.text_input("Coin")
        QtyCoin = st.number_input("QtyCoin", format="%.10f")
        rate = st.number_input("Rate", format="%.10f")
        
        button = st.form_submit_button("Submit")
        
        if button:
            QtyCoin = -1 * QtyCoin
            input_data(date,0,rate , 0, coin, QtyCoin, selectedcategory)
            st.success("Berhasil input.")
            
            
