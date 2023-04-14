import streamlit as st 
import altair as alt
import plotly.express as px 

# EDA Packages
import pandas as pd 
import numpy as np 
from datetime import datetime

# Utils
import joblib 
pipe_lr = joblib.load(open("Twitter_Sentiment_Analysis_Web_App (1) (2).pk1","rb"))

# Fxn
def predict_emotions(docx):
	results = pipe_lr.predict([docx])
	return results[0]

def get_prediction_proba(docx):
	results = pipe_lr.predict_proba([docx])
	return results

hide_streamlit_style = """
            <style>
	    #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def create_footer():
    st.markdown("<div style='height: 7vh'></div>", unsafe_allow_html=True)
    footer_container = st.container()
    left_col, right_col = footer_container.columns(2)
    with left_col:
        st.write("")
    with right_col:
        st.write("Group 3")

    st.markdown(
        """
        <script>
        const footer = document.getElementsByTagName('footer')[0];
        const appBody = document.getElementsByClassName('streamlit-container')[0];
        footer.style.position = 'fixed';
        footer.style.bottom = '0';
        appBody.style.paddingBottom = footer.offsetHeight + 'px';
        </script>
        """,
        unsafe_allow_html=True
    )

create_footer()

# Main Application
def main():
	st.title("tweets classification")
	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Home":
		st.subheader("Home-tweets In Text")

		with st.form(key='tweets_clf_form'):
			raw_text = st.text_area("Type Here")
			submit_text = st.form_submit_button(label='Submit')

		if submit_text:
			col1,col2  = st.columns(2)

			# Apply Fxn Here
			
			prediction = predict_emotions(raw_text)
			probability = get_prediction_proba(raw_text)

			with col1:
				st.success("Original Text")
				st.write(raw_text)

				st.success("Prediction")
				st.write("{}".format(prediction))


			with col2:
				st.success("Prediction Probability")
				st.write(probability)

	else:
		st.subheader("About")
		st.write("Welcome to our tweet sentiment dectection project! Our group has created a sophisticated machine learning model that can reliably recognise and categorize spam messages. With our spam classifier")
		
				# st.write(probability)
				proba_df = pd.DataFrame(probability,columns=pipe_lr.classes_)
				
	else:
		st.subheader("About")
		st.write("My name is seyi ogunmusire ")





if __name__ == '__main__':
	main()
