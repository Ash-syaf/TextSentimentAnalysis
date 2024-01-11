import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go

def displayPage():
  st.subheader("Text Analysis using Text to Emotion Algorithm")
  st.text("Enter the text to be analyzed")
  userText = st.text_input("User input", placeholder="Input the text here")
  st.text("")
  if st.button("Predict"):
    if (userText != ""):
      st.components.v1.html("""<h3 style="color:#0284c7; font-family:Source Sans Pro,sans-serif; font-size:28px; margin-bottom:8px; margin-top:55px;">RESULT</h3>""", height=150)
      getSentiment(userText)

def getSentiment(userText):
  emotion = te.get_emotion("Happy")
  #emotion1 = dict()
  #col1, col2, col3, col4, col5 = st.columns(5)
  #col1.metric("Happy1", None)
  #col2.metric("Sad", None)
  #col3.metric("Angry", None)
  #col4.metric("Fear", None)
  #col5.metric("Surprise", None)
  #print(emotion1)
  print(emotion)
  #plotBar(list(emotion1.keys()), list(emotion1.values()))

def plotBar(labels, values):
  f = go.figure(go.Bar(x = labels, y = values))
  st.plotly_chart(f)
