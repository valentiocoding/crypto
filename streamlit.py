import streamlit as st


input = st.Page(
    page="input.py",
    title="Input",
    icon="📝"
)

dashboard = st.Page(
    page="dashboard.py",
    title="Dashboard",
    icon="📊",
    default=True
)

tools = st.Page(
    page="tools.py",
    title="Estimate Profit Tools",
    icon="🔧"
)

pg = st.navigation({
    "Crypto": [dashboard, tools,input]
})


pg.run()