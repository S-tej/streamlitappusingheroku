# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 20:41:45 2024

@author: swara
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
diabetes_model=pickle.load(open('diabetes_model.sav','rb'))
heart_model=pickle.load(open("heart_disease_model.sav",'rb'))


#sidebar for navigation

with st.sidebar:
    
    selected=option_menu("Multi Disease Prediction System",['Diabetes Prediction','Heart Disease Prediction'],icons=['activity','heart'],default_index=0)
    #Here icons are the names of icons in bootstrap icons
    
#Diabetes prediction page
if(selected=='Diabetes Prediction'):
    
    #title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the users
    #columns for input field
    col1,col2,col3=st.columns(3)
    
    with col1:
        pregnancies=st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose=st.text_input('Glucose Level')
        
    with col3:
        BloodPresuure=st.text_input('Blood Pressure value')
    
    with col1:
        skinThickness=st.text_input('Skin Thickness value')
        
    with col2:
        Insulin=st.text_input('Insulin Level')
        
    with col3:
        BMI=st.text_input('BMI value')
        
    with col1:
        DiabetesPedigree=st.text_input('Diabtes Pedigree Function Value')
    
    with col2:
       Age=st.text_input('Age of the person') 
    
    
    #code for prediction
    diab_diagnosis=''
    
    #creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[pregnancies,Glucose,BloodPresuure,skinThickness,Insulin,BMI,DiabetesPedigree,Age]])
    
        if(diab_prediction[0]==1):
            diab_diagnosis='The person is diabetic'
            
        else:
            diab_diagnosis='The person is non diabetic'
            
    st.success(diab_diagnosis)
    
    
    
elif(selected=='Heart Disease Prediction'):
    
    #title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
   
    with col1:
       age = st.text_input('Age')
       
    with col2:
       sex = st.text_input('Sex')
       
    with col3:
       cp = st.text_input('Chest Pain types')
       
    with col1:
       trestbps = st.text_input('Resting Blood Pressure')
       
    with col2:
       chol = st.text_input('Serum Cholestoral in mg/dl')
       
    with col3:
       fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
       
    with col1:
       restecg = st.text_input('Resting Electrocardiographic results')
       
    with col2:
       thalach = st.text_input('Maximum Heart Rate achieved')
       
    with col3:
       exang = st.text_input('Exercise Induced Angina')
       
    with col1:
       oldpeak = st.text_input('ST depression induced by exercise')
       
    with col2:
       slope = st.text_input('Slope of the peak exercise ST segment')
       
    with col3:
       ca = st.text_input('Major vessels colored by flourosopy')
       
    with col1:
       thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
       
       
    
    
    # code for Prediction
    heart_diagnosis = ''
   
    # creating a button for Prediction
   
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
       
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
       
    st.success(heart_diagnosis)