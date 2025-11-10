#Button#
import streamlit as st
st.markdown("""
1. Saskia Putri Ananda - 0110222159
2. Rahmi Atika - 0110222279
3. Noer Muhammad Ayub - 0110222142
""")
st.title('Creating a Button')

# Defining a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the button')
else:
    st.write('You have not clicked the button')

#Radio Button#
import streamlit as st
st.title('Creating Radio Buttons')

# Defining Radio Button
gender = st.radio(
"Select your Gender",
('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selectes Others.")

#Check Boxes#
import streamlit as st
st.title('Creating Checkboxes')
st.write('Select your Hobies:')

#defining checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movie')
check_3 = st.checkbox('Sports')

#dropdwons#
import streamlit as st
st.title('Creating Dropdown')

#creating dropdown
hobby = st.selectbox('Choose your hobby: ',
('Books', 'Movies', 'Sports'))

#multiselects#
import streamlit as st
st.title('Multi-Select')

#defining multi_select  with pre-selection
hobbies = st.multiselect(
'What are your Hobbies',
['Reading', 'Cooking', 'Watching Movies/Tv Series', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Playing'])

#download buttons#
import streamlit as st
st.title("Download Button")

#Creating download button
down_btn = st.download_button(
label="Download Image",
data=open("C:/Dokumen/Kupu Kupu.jpg", "rb"),
file_name="download.jpg",
mime="image/jpg"
)

#Progress Bars#
import streamlit as st
import time
st.title('Progress Bar')

#deining progress bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

#Spinners#
import streamlit as st
import time
st.title('Spinner')

#defininng Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')