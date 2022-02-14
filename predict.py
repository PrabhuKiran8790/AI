import decimal
from os import device_encoding
from zipfile import Path
import streamlit as st
import pickle
import numpy as np
import joblib, os
from PIL import Image

# col1, col2, col3 = st.columns([3, 6, 1])
# with col1:
#     sru_logo = st.image(Image.open('sr-university-logo.png'), use_column_width='auto', output_format='png')

# with col2:
#     pass

# with col3:
#     ai_logo = st.image(Image.open('SRU_AI_LOGO_digital_art_x4_colored_toned.jpg'), width=80, output_format='png')




def prediction_model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))

model = pickle.load(open('DevSalaryPredDTR.model', 'rb'))




# le_country = data["le_country"]
# le_education = data["le_education"]
# le_MiscTechHaveWorkedWith = data["le_MiscTechHaveWorkedWith"]
# le_DevType = data["le_DevType"]
# le_LanguageHaveWorkedWith = data["le_LanguageHaveWorkedWith"]
def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = {
        'United States of America': 15,
        'India': 5,
        'United Kingdom': 14,
        'Canada': 2,
        'Australia': 0,
        'Germany': 4,
        'France': 3,
        'Turkey': 13,
        'Brazil': 1,
        'Italy': 6,
        'Russian Federation': 10,
        'Poland': 9,
        'Netherlands': 8,
        'Spain': 11,
        'Sweden': 12,
        'Mexico': 7
    }

    education_level = {
        'Bachelor’s degree': 0,
        'Less than a Bachelors': 1,
        'Master’s degree': 2,
        'Post grad': 3,
    }
            
    techknown = {
        'Machine Learning (NumPy, Pandas, TensorFlow, Keras, etc.)': 2,
        'Apache Spark, Hadoop': 1,
        'React Native/Flutter': 4,
        '.NET Framework': 0,
        'Other': 3,
    }
    
    devtype = {
        'Back-End Developer': 0,
        'Full-Stack Developer': 5,
        'Gaming/Graphics Developer': 6,
        'Data Science/Machine Learning Developer': 1,
        'DevOps Specialist': 3,
        'Front-End Developer': 4,
        'Database Administrator': 2,
        'Mobile Developer': 7,
        'Product Manager': 9,
        'Other': 8
    }   
    
    Languages = {
        'HTML/CSS, JavaScript, Node.js': 1,
        'C/C++': 0,
        'Python, Go': 5,
        'Java': 2,
        'Kotlin, Swift': 3,
        'Other': 4
    }
    
    webframe = {
        'Ruby on Rails': 4,
        'React.js/Spring/Vue.js/Gatsby': 3,
        'jQuery/Express': 5,
        'Django/Flask': 1,
        'Angular/Angular.js': 0,
        'Other': 2,
    }      
    
    
    with st.form("Inputs"):
        country = st.selectbox("Country", countries.keys())
        education = st.selectbox("Education Level", education_level.keys())
        techknown_ = st.selectbox("Technologies Worked with", techknown.keys())
        developerType = st.selectbox("Developer Type", devtype.keys())
        Languagesknown = st.selectbox("Languages Known", Languages.keys())
        webframeknown = st.selectbox("Web Framework", webframe.keys())
        expericence = st.slider("Years of Experience", 0, 50, 3)
    
    
        ok = st.form_submit_button("Calculate Salary")
        
        country = countries.get(country)
        education = education_level.get(education)
        techknown_ = techknown.get(techknown_)
        developerType = devtype.get(developerType)
        Languagesknown = Languages.get(Languagesknown)
        webframeknown = webframe.get(webframeknown)
    
    
        if ok:
            X = np.array([[country,
                        education,
                        expericence,
                        developerType,
                        Languagesknown,
                        techknown_,
                        webframeknown]])
                    
            X = X.astype(float)

            salary = model.predict(X)
            st.subheader(f"The estimated salary is ${salary[0]:.2f}")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
