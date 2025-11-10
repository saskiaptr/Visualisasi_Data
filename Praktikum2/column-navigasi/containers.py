import streamlit as st
import numpy as np
st.title("container")


st.write("Kelompok 28 - Visualisasi Data")
st.markdown(""" 
- Saskia Putri Ananda - 0110222159
- Rahmi Atika - 011022279
- Noer Muhammad Ayub - 011022142         
""")

with st.container():
    st.write("elemen inside container")
    st.line_chart(np.random.randn(40, 4))
    st.write("element outside container")

container_one = st.container()
container_one.write("elemen one inside container")
st.write("element outside container")

container_one.write("element teo inside container")
container_one.line.chart(np.random.randn(40, 4))
