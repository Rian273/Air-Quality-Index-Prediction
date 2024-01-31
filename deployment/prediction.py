# import libraries
import pandas as pd
import numpy as np
import streamlit as st
import joblib
from PIL import Image

# import pickle
import pickle

with open('model.pkl', 'rb') as file_1:
        model = pickle.load(file_1)

def run():
    # Load All Files
    # set the title
    st.title("Air Quality Index Prediction")
    st.write('---')

    st.image('https://www.alexandriava.gov/sites/default/files/styles/crop_card_image/public/2023-06/air%20quality%20index%20graphic%20shutterstock.jpg?itok=_OO015em')

    with st.expander("Keterangan Parameter"):
        st.write('Setiap parameter memiliki satuan nilai µg/m³ dan dapat diisikan dengan nilai float')
    
    with st.form(key='form parameter'):
        City = st.selectbox(label='Pilih Nama Kota', options=['Ahmedabad', 'Amaravati', 'Amritsar', 'Bengaluru', 'Chandigarh',
                                                              'Chennai', 'Coimbatore', 'Delhi', 'Gurugram', 'Hyderabad',
                                                              'Jaipur', 'Kolkata', 'Lucknow', 'Patna', 'Shillong', 'Talcher',
                                                              'Visakhapatnam']),
        PM25 = st.number_input(label='Masukkan Nilai PM2.5 (µg/m³)', min_value=0.00,max_value=1000.00),
        PM10 = st.number_input(label='Masukkan Nilai PM10 (µg/m³)', min_value=0.00,max_value=1000.00),
        NO = st.number_input(label='Masukkan Nilai NO (µg/m³)', min_value=0.00,max_value=1000.00),
        NO2 = st.number_input(label='Masukkan Nilai NO2 (µg/m³)', min_value=0.00,max_value=1000.00),
        NOx = st.number_input(label='Masukkan Nilai NOx (µg/m³)', min_value=0.00,max_value=1000.00),
        NH3 = st.number_input(label='Masukkan Nilai NH3 (µg/m³)', min_value=0.00,max_value=1000.00),
        CO = st.number_input(label='Masukkan Nilai CO (µg/m³)', min_value=0.00,max_value=1000.00),
        SO2 = st.number_input(label='Masukkan Nilai SO2 (µg/m³)', min_value=0.00,max_value=1000.00),
        O3 = st.number_input(label='Masukkan Nilai O3 (µg/m³)', min_value=0.00,max_value=1000.00),
        Benzene = st.number_input(label='Masukkan Nilai Benzene (µg/m³)', min_value=0.00,max_value=1000.00),
        Toluene = st.number_input(label='Masukkan Nilai Toluene (µg/m³)', min_value=0.00,max_value=1000.00),
        Xylene = st.number_input(label='Masukkan Nilai Xylene (µg/m³)', min_value=0.00,max_value=1000.00)

        submit = st.form_submit_button("Predict")

    st.write('Berikut adalah hasil dari input yang telah dimasukkan :')

    data_inf = pd.DataFrame({
         'City' : City,
         'PM2.5' : PM25,
         'PM10' : PM10,
         'NO' : NO, 
         'NO2' : NO2, 
         'NOx' : NOx,
         'NH3' : NH3, 
         'CO' : CO, 
         'SO2' : SO2, 
         'O3' : O3, 
         'Benzene' : Benzene, 
         'Toluene' : Toluene,
         'Xylene' : Xylene
         }, index=[0])

    st.table(data_inf)

    if submit:
        prediction =  model.predict(data_inf)

        if prediction[0] == 0:
            prediction = 'Poor Air Quality'
        else:
            prediction = 'Good Air Quality'

        st.subheader('Air Quality Result :')
        st.subheader(prediction)

if __name__ == "__name__":
     run()