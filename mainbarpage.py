import streamlit as st
import sidebarpage
import textblobalgo
import texttoemotion
import vaderalgo
page = sidebarpage.show()
if (page == 'TextBlob Analysis'):
  textblobalgo.displayPage()
#elif (page == 'Text2Emotion Analysis'):
  #texttoemotion.displayPage()
elif page == 'VADER Sentiment Analysis':
  vaderalgo.displayPage()
