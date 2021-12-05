import streamlit as st
st.set_page_config(page_title="Software Developer Salary Prediction", page_icon="📉")

from PIL import Image
from predict import show_predict_page
from explore_page import show_explore_page


image = Image.open('icon.png')
img = st.sidebar.image(image, width=80, use_column_width=80)
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

about  = st.sidebar.markdown('''
## ABOUT
This is Machine Learning Web Application that helps in Predicting the Salary of a Software Developer based on their Experience, Location, Education Level, Languages known etc,\n

Code: [source](https://github.com/prabhuKiran8790/AI/CapstoneProject)\n

Web Application made with [Streamlit](https://streamlit.io/)
''')

if page == "Predict":
    show_predict_page()

else:
    show_explore_page()
    
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)