import datetime
from google.oauth2 import service_account
import streamlit as st
import gspread
import pandas as pd

def get_data():
    google_cloud_secrets = st.secrets["google_api"]

    creds = service_account.Credentials.from_service_account_info(
        {
            "type": google_cloud_secrets["type"],
            "project_id": google_cloud_secrets["project_id"],
            "private_key_id": google_cloud_secrets["private_key_id"],
            "private_key": google_cloud_secrets["private_key"].replace("\\n", "\n"),
            "client_email": google_cloud_secrets["client_email"],
            "client_id": google_cloud_secrets["client_id"],
            "auth_uri": google_cloud_secrets["auth_uri"],
            "token_uri": google_cloud_secrets["token_uri"],
            "auth_provider_x509_cert_url": google_cloud_secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": google_cloud_secrets["client_x509_cert_url"],
            "universe_domain": google_cloud_secrets["universe_domain"],
        },
        scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    )


    client = gspread.authorize(creds)
    spreadsheet_id = "1NB2f62PEkps0KhkRzqX2AhCUQN0-RGqHdv5mhanoWj4"

    data = client.open_by_key(spreadsheet_id).worksheet('transaction').get_all_records()

    pd.set_option('display.float_format', '{:.10f}'.format)

    data = pd.DataFrame(data)
    return data




data = get_data()




def input_data(date, rupiah, rate, usdt, coin, qty_coin,   keterangan):
    google_cloud_secrets = st.secrets["google_api"]

    creds = service_account.Credentials.from_service_account_info(
        {
            "type": google_cloud_secrets["type"],
            "project_id": google_cloud_secrets["project_id"],
            "private_key_id": google_cloud_secrets["private_key_id"],
            "private_key": google_cloud_secrets["private_key"].replace("\\n", "\n"),
            "client_email": google_cloud_secrets["client_email"],
            "client_id": google_cloud_secrets["client_id"],
            "auth_uri": google_cloud_secrets["auth_uri"],
            "token_uri": google_cloud_secrets["token_uri"],
            "auth_provider_x509_cert_url": google_cloud_secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": google_cloud_secrets["client_x509_cert_url"],
            "universe_domain": google_cloud_secrets["universe_domain"],
        },
        scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    )


    client = gspread.authorize(creds)
    spreadsheet_id = "1NB2f62PEkps0KhkRzqX2AhCUQN0-RGqHdv5mhanoWj4"

    sheet = client.open_by_key(spreadsheet_id).worksheet('transaction')

    date = date.strftime('%d/%m/%Y')
    data = [
        date, rupiah,  rate, usdt, coin, qty_coin, keterangan
    ]

    sheet.append_row(data)




def edit_data(data):
    google_cloud_secrets = st.secrets["google_api"]

    creds = service_account.Credentials.from_service_account_info(
        {
            "type": google_cloud_secrets["type"],
            "project_id": google_cloud_secrets["project_id"],
            "private_key_id": google_cloud_secrets["private_key_id"],
            "private_key": google_cloud_secrets["private_key"].replace("\\n", "\n"),
            "client_email": google_cloud_secrets["client_email"],
            "client_id": google_cloud_secrets["client_id"],
            "auth_uri": google_cloud_secrets["auth_uri"],
            "token_uri": google_cloud_secrets["token_uri"],
            "auth_provider_x509_cert_url": google_cloud_secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": google_cloud_secrets["client_x509_cert_url"],
            "universe_domain": google_cloud_secrets["universe_domain"],
        },
        scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    )


    client = gspread.authorize(creds)
    spreadsheet_id = "1NB2f62PEkps0KhkRzqX2AhCUQN0-RGqHdv5mhanoWj4"
    sheet = client.open_by_key(spreadsheet_id).worksheet('transaction').clear()
    values = [data.columns.tolist()] + data.values.tolist()
    sheet = client.open_by_key(spreadsheet_id).worksheet('transaction').update('A1',values)
