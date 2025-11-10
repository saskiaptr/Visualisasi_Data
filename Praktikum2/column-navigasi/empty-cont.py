import streamlit as st
import time

st.write("Kelompok 28 - Visualisasi Data")
st.markdown(""" 
- Saskia Putri Ananda - 0110222159
- Rahmi Atika - 011022279
- Noer Muhammad Ayub - 011022142         
""")

with st.empty():
    for seconds in range(5):
        st.wirte(f"{seconds} seconds have passed")
        time.sleep(1)
        st.write("timw up!")
        