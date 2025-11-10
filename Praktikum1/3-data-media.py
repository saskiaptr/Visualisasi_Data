import streamlit as st
st.markdown("""
1. Saskia Putri Ananda - 0110222159
2. Rahmi Atika - 0110222279
3. Noer Muhammad Ayub - 0110222142
""")
st.write("Displaying an Images")

#displaying image by specifying path
st.image("C:/Dokumen/Kupu Kupu.jpg")

#image courtesy by unplash
st.write("image Countesy: unplash.com")

#image courtesy
st.write("Displaying Multiple Images")

#listing out animal images
animal_images = [
'C:/Dokumen/Semester 7/Visualisasi Data/assets/animal1.jpeg',
'C:/Dokumen/Semester 7/Visualisasi Data/assets/animal2.jpg',
'C:/Dokumen/Semester 7/Visualisasi Data/assets/animal3.jpg',
'C:/Dokumen/Semester 7/Visualisasi Data/assets/animal4.jpg',
]

#dispalay multiple image with width 150
st.image(animal_images, width=150)

#image courtesy
st.write("Image Courtesy: Unplash")

#backgroun image#
import streamlit as st
import base64

#Function to set Image as Background
def add_local_backgound_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unplash")
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("Background Image")

#Calling Image in function
add_local_backgound_image_('C:/Dokumen/Semester 7/Visualisasi Data/assets/animal4.jpg')

#Resizing an image#
import streamlit as st
from PIL import Image

original_image = Image.open("C:/Dokumen/Semester 7/Visualisasi Data/assets/animal3.jpg")
#display original image
st.title("Original Image")
st.image(original_image)
#resizing image to 600*400
resized_image = original_image.resize((600, 400))
#displaying resize image
st.title("Resized Image")
st.image(resized_image)