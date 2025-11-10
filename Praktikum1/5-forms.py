#text Bos#
import streamlit as st
st.markdown("""
1. Saskia Putri Ananda - 0110222159
2. Rahmi Atika - 0110222279
3. Noer Muhammad Ayub - 0110222142
""")
st.title("Text Box")

#Creating Text Box
name = st.text_input("Enter your Name")
st.write("Your Name is ", name)

#text area#
import streamlit as st

#creating text area
input_text = st.text_area('Enter your Review')
#printing entered text
st.write("""You entered: \n""",input_text)

#number input#
import streamlit as st
#create number input
st.number_input("Enter your Number")
num = st.write("Min. Value is 0, n\ Max. value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)


#Time#
import streamlit as st
st.title("Time")

#defining time function
st.time_input("Select Your Time")

#Date#
import streamlit as st
st.title("Date")

#defining date funcation
st.date_input("Select Date")
import streamlit as st
import datetime
st.title("Date")

#defining time function
st.date_input("Select Your Date", value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))


#color#
import streamlit as st
st.title("Select Color")

#defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

#dataset upload#
import streamlit as st
import pandas as pd 
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV",type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,
        "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
else:
    st.write("No CSV File is Uploaded")


#submiit button#
import streamlit as st
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')

#defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)