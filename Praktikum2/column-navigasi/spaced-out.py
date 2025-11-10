import streamlit as st
from PIL import Image

st.write("Kelompok 28 - Visualisasi Data")
st.markdown(""" 
- Saskia Putri Ananda - 0110222159
- Rahmi Atika - 011022279
- Noer Muhammad Ayub - 011022142         
""")

img = Image.open("C:/Dokumen/Kupu Kupu.jpg")
st.title("Spaced-Out Columns")

for _ in range(2):

    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)