# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:42:09 2024

@author: praka
"""

import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open('C:/Users/praka/Downloads/trained_model.sav', 'rb'))

# Creating a function for prediction
def mail_prediction(input_data):
    input_mail = ["Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."]

    # Assuming 'feature_extraction' is a previously defined object used for transforming the input
    input_data_features = feature_extraction.transform(input_mail)
    prediction = loaded_model.predict(input_data_features)
    return prediction

def main():
    # Giving a title
    st.title('MAIL PREDICTION WEBAPP')
    
    # Getting input data from the user
    ham = st.text_input("ham message")
    spam = st.text_input("spam message")
     
    # Code for prediction
    prediction = ''
    
    # Creating a button for prediction
    if st.button('Mail prediction result'):
        prediction = mail_prediction([ham, spam])
    st.success(prediction)

if __name__ == '__main__':
    main()
