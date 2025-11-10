import streamlit as st
st.sidebar.title("sidebar")

st.write("Kelompok 28 - Visualisasi Data")
st.markdown(""" 
- Saskia Putri Ananda - 0110222159
- Rahmi Atika - 011022279
- Noer Muhammad Ayub - 011022142         
""")

st.sidebar.radio("are u a new user", ["yes", "no"])
st.sidebar.slider("select a number", 0,10)
