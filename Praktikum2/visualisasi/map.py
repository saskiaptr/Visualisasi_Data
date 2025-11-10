import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Kelompok 28 - Visualisasi Data")
st.markdown(""" 
- Saskia Putri Ananda - 0110222159
- Rahmi Atika - 011022279
- Noer Muhammad Ayub - 011022142         
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/(10, 10) + (15.3439, 75.4579),
    columns=("latitude", "longitude")
)

st.map(df)