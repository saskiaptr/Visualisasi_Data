# import library yang dibutuhkan
import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd # type: ignore
import numpy as np # type: ignore
import altair as alt # type: ignore

st.markdown("""
1. Saskia Putri Ananda - 0110222159
2. Rahmi Atika - 0110222279
3. Noer Muhammad Ayub - 0110222142
""")


#defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(30,10),
columns=('col_no %d' % i for i in range(10)))
#menampilkan dataframe
st.dataframe(df)

import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd # type: ignore
import numpy as np # type: ignore
df = pd.DataFrame(
np.random.randn(30, 10),
columns=('col_no %d' % i for i in range(10)))
#highlight nilai terkecil disetiap kolom dataframe
#axis=0 berkerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

#tabel statis#
import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd # type: ignore
import numpy as np # type: ignore
st.subheader("Tabel statistis")
df = pd.DataFrame(
np.random.randn(30,10),
columns=('col_no %d' % i for i in range(10)))
#defining data in  table
st.table(df)

#metrics#
import streamlit as st # pyright: ignore[reportMissingImports]
#defining columns
c1, c2, c3 = st.columns(3)
#defining metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Tress", "91456", "-1132649")

#the write () function as a superfunction
import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd # type: ignore
import numpy as np # type: ignore
df = pd.DataFrame(
np.random.randn(30, 10),
columns=('col_no %d' % i for i in range(10)))
#definig multiple argumens in write funcation
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

#importing necessary libraries
import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd # type: ignore
import numpy as np # type: ignore
import altair as alt # type: ignore
#defining random values for chart
df = pd.DataFrame(
np.random.randn(10, 2),
columns=['a', 'b'])

#magic#
#math calculations with no functions defined
"Adding 5 & 4 =", 5+4
#displaying variabel 'a' and its value
a = 5
'a', a
#markdown with magic
"""
# Magic Fearur
Markdown working witghout defining its function explicitly.
"""

#dataframe using magic
import pandas as ps
df = pd.DataFrame({'col': [1,2]})
'dataframe', df

#magic working on charts
import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)

#magic chart
"chart", chart