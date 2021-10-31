# Core Pkgs
import streamlit as st
import sklearn
import joblib,os
import numpy as np 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
import plotly.express as px
import seaborn as sns



# Loading Models
def load_prediction_model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))

def main():
	"""Linear regression"""

	st.title("Bicarbonate Estimation using Linear Regression and SGD Optimization")

	# html_templ = """
	# <div style="background-color:#0e1117;padding:10px;">
	# <h3 style="color:White">Polynomial Regression Model to Estimate bicarbonates from pH level</h3>
	# </div>
	# """

	# st.markdown(html_templ,unsafe_allow_html=True)

	activity = ("Bicarbonate Estimation","Dataset","About")
	choice = st.sidebar.selectbox("Menu",activity)

# Bicarbonate Estimation CHOICE
	if choice == 'Bicarbonate Estimation':

		st.subheader("Bicarbonate Estimation")

		ph_level = st.slider("pH of the Water",0.0,10.0)

		#st.write(type(experience))

		if st.button("Estimate:"):

			# regressor = load_prediction_model("model.pkl")
			# experience_reshaped = np.array(experience).reshape(-1,1)

			#st.write(type(experience_reshaped))
			#st.write(experience_reshaped.shape)

			# predicted_salary = regressor.predict(experience)
			
			model = pickle.load(open('Assignment4_sgd.pkl', 'rb'))
			# user_ip=input('enter pH level: ')
			level = np.array(float(ph_level))
			level = level.reshape(-1,1)
			# level_features =  poly_reg.fit_transform(level)
			bicarbonates = model.predict(level)
			#print('Bicarbonate Levels: ',bicarbonates)
			st.info("Bicarbonate with {} pH of the Water: {}".format(ph_level, bicarbonates))


	if choice == 'Dataset':
		dataframe = pd.read_csv('pH-Bicarbonate.csv')
		dataframe.rename(columns={"X": "pH of the Water", "Y":"Bicarbonates"}, inplace=True)
		st.subheader("pH vs Bicarbonates Dataset")
		st.write(dataframe)
		fig = px.scatter(
			x=dataframe["pH of the Water"],
			y=dataframe["Bicarbonates"])
		fig.update_layout(
			xaxis_title="pH of the Water",
			yaxis_title="Bicarbonates")
		st.write(fig)

		


	# About CHOICE
	if choice == 'About':
		st.subheader("About")
		st.markdown("""
			## Linear Regression to Estimate Bicarbonates from pH Level of the Water
			
			##### By
			+ **[GitHub/PrabhuKiran8790](https://www.github.com/PrabhuKiran8790/)**
			+ [prabhukiran426@gmail.com](mailto:prabhukiran426@gmail.com)

			""")


if __name__ == '__main__':
	main()