import streamlit as st
from PIL import Image


uploaded_image = st.file_uploader("Upload image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)
    
    # Convert the image to Grayscale
    gray_img = img.convert("L")
    
    # Render the grayscale image
    st.image(gray_img)

elif uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)