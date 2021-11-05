import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns
import streamlit as st
import plotly.express as px
import pickle
import joblib,os




# Loading Models
def load_prediction_model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))


def main():
    st.title("Estimating Electrical Load based on the Last previous three loads")
    
    data = pd.read_csv('load_data_modified.csv')
     
    activity = ("Load Prediction⚡",
                "Dataset Insights📊",
                "Model Info",
                "About")
    choice = st.sidebar.selectbox("Menu",activity)

    if choice == 'Load Prediction⚡':
        
        st.text("Enter Loads in KW.(Ex. 4523 KW)")
        load1  = st.text_input("Enter Load(KW) at T-3 hrs")
        load2  = st.text_input("Enter Load(KW) at T-2 hrs")
        load3  = st.text_input("Enter Load(KW) at T-1 hrs")
        
        if st.button("Predict the load"):
            model = pickle.load(open('mlrmodel.model', 'rb'))
            out_load = model.predict([[load1, load2, load2]])
            st.success("The Estimated load is {} KW".format(round(out_load[0], 4)))
            
        
            
        dataframe_show = st.checkbox("Show Dataset")
        if dataframe_show:
            data = pd.read_csv('load_data_modified.csv')
            data = data.rename(columns={
            'X1':'L(t-3) KW',
            'X2':'L(t-2) KW',
            'X3':'L(t-1) KW',
            'Y':'L(t) KW'})
            st.dataframe(data)
            
        st.markdown("`Click on the Sidebar to Navigate to the Menu`")
            
    if choice == 'Dataset Insights📊':
        pairplot = st.checkbox("Pair Plot")
        if pairplot:
            title= 'Plots'
            fig = px.scatter_matrix(data)
            fig.update_layout(title=title,
                        dragmode='select',
                        width=1000,
                        height=1000,
                        hovermode='closest')
            st.write(fig)
        dataframe_show = st.checkbox("Show Dataset")
        if dataframe_show:
            data = pd.read_csv('load_data_modified.csv')
            data = data.rename(columns={
            'X1':'L(t-3) KW',
            'X2':'L(t-2) KW',
            'X3':'L(t-1) KW',
            'Y':'L(t) KW'})
            st.dataframe(data)
            
    if choice == 'Model Info':
        st.markdown("""
        ## Model Information
        ---
        This is a simple web application to Estimate the Load at a particular hour based on the last three Electrical Loads based on the Multiple Linear regression.  
          
        Historical load data at each hour of the day for the period from September-2018 to November-2018 was taken from
        33/11 kV substation near Kakatiya University in Warangal. The time series data-set consists of a total of 2184 samples.  It has been observed that load data distribution follows the normal distribution with a mean value of 6028 kW and a standard deviation of 1066 kW. Out of 2184 load samples in the specified time period, 95% of data points were falling between 5983 and 6072 kW  
        
        [Link to dataset](https://data.mendeley.com/datasets/ycfwwyyx7d/2?__cf_chl_captcha_tk__=pmd_xbBVZco5j0U[%E2%80%A6]i6qHihCo_rxLe6xP2O.KRLeb_s-1632990782-0-gqNtZGzNAtCjcnBszQt9)             
                    """)
        
    if choice == 'About':
        st.subheader("About")
        st.markdown("""
            ## Estimating Electrical Load based on the previous 3 hours load at a particular hour  
            ---
            ##### By
            + **[GitHub/PrabhuKiran8790](https://www.github.com/PrabhuKiran8790/)**
            + [prabhukiran426@gmail.com](mailto:prabhukiran426@gmail.com)

            """)
    
            
if __name__ == '__main__':
    main()