<<<<<<< HEAD
# Core Packages
=======
# Core Pkgs
>>>>>>> ad426a6e06065ffa88bee3a5a6edf6d54c087e10
import streamlit as st 
import altair as alt
import plotly.express as px 

<<<<<<< HEAD
# EDA Packages
=======
# EDA Pkgs
>>>>>>> ad426a6e06065ffa88bee3a5a6edf6d54c087e10
import pandas as pd 
import numpy as np 
from datetime import datetime

<<<<<<< HEAD
# Utils
import joblib 
pipe_lr = joblib.load(open("Twitter_Sentiment_Analysis_Web_App (1) (2).pk1","rb"))

# Fxn
def predict(docx):
=======
from track_utils import create_page_visited_table,add_page_visited_details,view_all_page_visited_details,add_prediction_details,view_all_prediction_details,create_emotionclf_table


# Utils
import joblib 
pipe_lr = joblib.load(open("Twitter_Sentiment_Analysis_Web_App.pkl",'rb'))

# Fxn
def predict_emotions(docx):
>>>>>>> ad426a6e06065ffa88bee3a5a6edf6d54c087e10
	results = pipe_lr.predict([docx])
	return results[0]

def get_prediction_proba(docx):
	results = pipe_lr.predict_proba([docx])
	return results

<<<<<<< HEAD
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
	st.title("Tweet sentiment App")
	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Home":
		st.subheader("text sentiment In Text")

		with st.form(key='tweet_sentiment_form'):
=======
# Main Application
def main():
	st.title("tweets classification")
	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Home":
		st.subheader("Home-tweets In Text")

		with st.form(key='tweets_clf_form'):
>>>>>>> ad426a6e06065ffa88bee3a5a6edf6d54c087e10
			raw_text = st.text_area("Type Here")
			submit_text = st.form_submit_button(label='Submit')

		if submit_text:
			col1,col2  = st.columns(2)

			# Apply Fxn Here
<<<<<<< HEAD
			prediction = predict(raw_text)
			probability = get_prediction_proba(raw_text)
			
=======
			prediction = predict_emotions(raw_text)
			probability = get_prediction_proba(raw_text)
			
			add_prediction_details(raw_text,prediction,np.max(probability),datetime.now())
>>>>>>> ad426a6e06065ffa88bee3a5a6edf6d54c087e10

			with col1:
				st.success("Original Text")
				st.write(raw_text)

				st.success("Prediction")
<<<<<<< HEAD
				st.write("{}".format(prediction))
=======
				emoji_icon = emotions_emoji_dict[prediction]
				st.write("{}:{}".format(prediction,emoji_icon))
				st.write("Confidence:{}".format(np.max(probability)))
>>>>>>> ad426a6e06065ffa88bee3a5a6edf6d54c087e10



			with col2:
				st.success("Prediction Probability")
<<<<<<< HEAD
				st.write(probability)

	else:
		st.subheader("About")
		st.write("Welcome to our tweet sentiment dectection project! Our group has created a sophisticated machine learning model that can reliably recognise and categorize spam messages. With our spam classifier")
		
=======
				# st.write(probability)
				proba_df = pd.DataFrame(probability,columns=pipe_lr.classes_)
				# st.write(proba_df.T)
				proba_df_clean = proba_df.T.reset_index()
				proba_df_clean.columns = ["emotions","probability"]

				fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions',y='probability',color='emotions')
				st.altair_chart(fig,use_container_width=True)

	else:
		st.subheader("About")
		st.write("My name is seyi ogunmusire ")





>>>>>>> ad426a6e06065ffa88bee3a5a6edf6d54c087e10
if __name__ == '__main__':
	main()
