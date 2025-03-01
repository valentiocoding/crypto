import sqlite3
import io
import pandas as pd
import streamlit as st
from database import get_data, edit_data
import time
import altair as alt

st.session_state.data = get_data()

if "data" not in st.session_state:
    st.session_state.data = get_data()

data = st.session_state.data

alltransaction = data

with st.expander("All Transaction"):
    editdata = st.data_editor(alltransaction,num_rows="dynamic")

    if st.button("Apply Edit"):
        final_data = editdata
        edit_data(final_data)

        data = get_data()

        with st.spinner("Editing..."):
            time.sleep(1)
            st.success("Edit Success")
            time.sleep(1)
            st.rerun()
            

    

st.title("Dashboard")
st.divider()

# withdraw = data[data['keterangan'] == 'Transfer to Bank Account']['rupiah'].sum()

st.subheader("USDT History")
total_topup = data[data['keterangan'] == 'Top Up Toko Crypto']['rupiah'].sum()
st.metric(label="Total Topup", value=f"Rp {total_topup:,.0f}", border=True)
# st.metric("Total Withdraw", f"{withdraw:,.0f}", border=True)
col1, col2 = st.columns(2)
total_usdt = data[data['keterangan'] == 'Buy USDT on Toko Crypto']['usdt'].sum()





# usdt = data['usdt'].sum()
col1.metric("Total Buy USDT", f"{total_usdt:,.10f}", border=True)

usdt_rate = data[data['keterangan'] == 'Buy USDT on Toko Crypto']['rate'].mean()
col2.metric("Average USDT Buy Rate", f"{usdt_rate:,.2f}", border=True)


with st.expander("See All USDT History"):
    usdt_history = data[data['keterangan'] == 'Buy USDT on Toko Crypto']
    usdt_history = usdt_history[['date', 'rate', 'usdt']]
    usdt_history['total_rupiah'] = usdt_history['rate'] * data['usdt']
    usdt_history.sort_values(by='date', ascending=False, inplace=True)
    usdt_history.reset_index(drop=True, inplace=True)
    st.write(usdt_history)
    st.line_chart(usdt_history, x='date', y='rate')

st.divider()

st.subheader("Coin History")

with st.expander("Coin List"):
    coin_list = data[data['keterangan'] == 'Buy Coin on Binance']
    coin_list = coin_list[['date','coin', 'QtyCoin', 'rate']]
    # coin_list['date'] = pd.to_datetime(coin_list['date']).dt.date
    coin_list.sort_values(by='date', ascending=False, inplace=True)
    st.dataframe(coin_list)
    
selected_coin = st.selectbox("Select Coin", coin_list['coin'].unique())

col1, col2 = st.columns(2)

total_buy_coin = data[(data['coin'] == selected_coin) & (data['keterangan'] == 'Buy Coin on Binance')]['QtyCoin'].sum()
col1.metric(f"Total {selected_coin} Buy", f"{total_buy_coin:,.10f}", border=True)
average_coin_rate = data[(data['coin'] == selected_coin) & (data['keterangan'] == 'Buy Coin on Binance')]['rate'].mean()
col2.metric(f"Average {selected_coin} Buy Rate", f"{average_coin_rate:,.2f}", border=True)
chart = coin_list[coin_list['coin'] == selected_coin]
chart['date'] = pd.to_datetime(chart['date'], format='%d/%m/%Y')
chart.sort_values(by='date', ascending=False, inplace=True)
chart.reset_index(drop=True, inplace=True)
line_chart = alt.Chart(chart).mark_line(point=True).encode(
    
    x=alt.X('date:T', axis=alt.Axis(format='%d/%m/%Y'), title='Date'),
    y=alt.Y('rate:Q', title='Rate'),
    # color=alt.Color('coin:N', title='Coin')
).interactive()
st.altair_chart(line_chart, use_container_width=True)

st.divider()