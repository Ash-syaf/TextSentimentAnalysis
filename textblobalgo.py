from textblob import TextBlob
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

#Create user defined function
def displayPage():
  st.subheader("Text Analysis using Text Blob")
  st.text("Enter the user text to be analysed")
  userText = st.text_input('Input', placeholder = 'Input the text here')
  st.text(' ')
  if st.button('Predict'):
    if (userText != ''):
      st.components.v1.html("""<h3 style="color:#0284c7; font-family:Source Sans Pro,sans-serif; font-size:28px; margin-bottom:8px; margin-top:55px;">RESULT</h3>""", height=150)
      getSentiment(userText)
      
#Write user define function getSentiment
def getSentiment(userText):
  polarity, subj, status = getPolarity(userText)
  if (status == "Positive"):
    image = Image.open('./images/positive.png')
  elif (status == 'Negative'):
    image = Image.open('./images/negative.png')
  else:
    image = Image.open('./images/neutral.png')
  col1, col2, col3 = st.columns(3)
  col1.metric("Polarity", polarity, None)
  col2.metric("Subjectivity", subj, None)
  col3.metric("Result", status, None)
  st.image(image, caption=status)

def getPolarity(userText):
  tb = TextBlob(userText)
  polarity = round(tb.polarity, 2)
  subj = round(tb.subjectivity, 2)
  if polarity > 0:
    return polarity, subj, "Positive"
  elif polarity == 0:
    return polarity, subj, "Neutral"
  else:
    return polarity, subj, "Negative"
