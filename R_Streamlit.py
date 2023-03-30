import streamlit as st
from PIL import Image

#title
st.title('R IN RAMADAN')


image1 =Image.open("coding.png")
st.image(image1)



# Add Video
st.write('''
##Day 1 (a)    
Installation Procedure''')
video1 = open("Installation.mp4","rb")
st.video(video1)



