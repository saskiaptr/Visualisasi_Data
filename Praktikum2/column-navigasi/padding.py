import streamlit as st
from PIL import Image

st.write("Kelompok 28 - Visualisasi Data")
st.markdown(""" 
- Saskia Putri Ananda - 0110222159
- Rahmi Atika - 011022279
- Noer Muhammad Ayub - 011022142         
""")

img = Image.open("C:/Dokumen/Kupu Kupu.jpg")
st.title("Padding")

col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)