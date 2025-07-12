import streamlit as st
import matplotlib.pyplot as plt
from cv_assignment_oil_sketch import process
from cv import apply_anime_filter
from sketch import sketch_image
from water_color import apply_watercolor_effect

#Background image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://papers.co/desktop/wp-content/uploads/papers.co-sm55-pastel-blue-red-morning-blur-gradation-29-wallpaper.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

#Use st.@st.cache_resource to cache the model to reduce time for loading pages
@st.cache_resource
def load_oil_model(image):
    return process(image)

@st.cache_resource
def load_anime_model(image):
    return apply_anime_filter(image)

@st.cache_resource
def load_sketch_model(image):
    return sketch_image(image)

@st.cache_resource
def load_water_model(image):
    return apply_watercolor_effect(image)

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Image to Painting Converter")

#Upload an image
uploaded_file = st.file_uploader("Choose a RGB or RGBA image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    inputImage = plt.imread(uploaded_file)

    flag=1
    if inputImage.ndim < 3:
        flag=0
        st.write('Only RGB or RGBA images supported.')
    elif inputImage.ndim == 4:
        inputImage = inputImage[:, :, :3]

    if flag==1:
        result= process(inputImage)
    
    #Display the uploaded image after converting to oil painting
    st.image(inputImage, caption='Uploaded Image', use_column_width=True)
    oil=load_oil_model(inputImage)
    st.write("")
    st.write("After Coversion to Painting")
    st.subheader('Oil Painting')
    st.image(oil, caption='Oil Painting', use_column_width=True)

    anime=load_anime_model(inputImage)
    st.write("")
    st.subheader('Anime Painting')
    st.image(anime, caption='Anime Painting', use_column_width=True)

    sketch=load_sketch_model(inputImage)
    st.write("")
    st.subheader('Pencil Sketch')
    st.image(sketch, caption='Pencil Sketch', use_column_width=True)

    water=load_water_model(inputImage)
    st.write("")
    st.subheader('Water Color Painting')
    st.image(water, caption='Water Color Painting', use_column_width=True)
