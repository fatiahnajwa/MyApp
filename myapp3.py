import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt


st.write("""
# Body fat Analysis for Women
This app help women to work out on their body fat!
""")

from PIL import Image
image = Image.open('women.jpg')
st.image(image)


st.sidebar.header('User Input Parameters')


def user_input_features():
  Name = st.sidebar.text_input('INSERT YOUR NAME')
  Age = st.sidebar.text_input('AGE')
  Weight = st.sidebar.text_input('WEIGHT(kg)')
  Height = st.sidebar.text_input('HEIGHT(cm)')
  Neck  = st.sidebar.text_input('NECK(cm)')
  Waist = st.sidebar.text_input('WAIST(cm)')
  Hip = st.sidebar.text_input('HIP(cm)')
  data = {'AGE': Age,
            'WEIGHT': Weight,
            'HEIGHT': Height,
          'NECK(cm)': Neck,
          'WAIST(cm)': Waist,
          'HIP(cm)':Hip}
  features = pd.DataFrame(data, index=[0])
  return features
df = user_input_features()
#df = user_input_features()

st.subheader('User Input parameters')
st.write(df)
st.header("Let see how you can work out on it...")
st.subheader('Enter your body fat percentage')
Bodyfat=st.text_input('')

from PIL import Image
image = Image.open('chart.png')
st.image(image)

st.subheader('THANK YOU!!!!')