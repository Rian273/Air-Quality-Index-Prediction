import streamlit as st
import eda
import prediction as prediction

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploratory Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page')
    st.image('https://www.epa.gov/sites/default/files/styles/medium/public/2021-05/aqaw_2021_0.png?itok=dMP6C0bR')
    st.write('Milestone 2')
    st.write('Nama      : Permata Hajjarianti')
    st.write('Batch     : HCK-011')
    st.write('Tujuan M2 : Memprediksi Kualitas Udara Kota-Kota di India')
    st.write('')
    st.caption('Silahkan pilih menu di Select Box pada sebelah kiri layar anda!')
    st.write('')
    st.write('')

    with st.expander("Latar Belakang"):
            st.caption('''Urgensi mengapa dilakukan prediksi kualitas udara kota-kota di India yaitu untuk mengatasi dampak serius dari kesalahan prediksi yang menyebabkan kualitas udara terlihat lebih baik daripada yang sebenarnya. Ketidakakuratan semacam itu berpotensi menghambat kebijakan pengelolaan lingkungan dan kesehatan masyarakat, karena otoritas dapat kesulitan mengambil tindakan preventif atau pencegahan yang tepat ketika kualitas udara sebenarnya buruk. Dalam situasi dimana banyak prediksi menunjukkan kondisi udara yang baik, padahal sebaliknya (buruk), risiko kesehatan masyarakat dapat terabaikan. Oleh karena itu, diperlukan pemahaman mendalam tentang pola dan tren dalam data kualitas udara, termasuk parameter-parameter kunci seperti PM2.5, PM10, NO, NO2, CO, dan parameter lainnya. Analisis ini bertujuan untuk mengembangkan model prediktif yang lebih akurat, mengurangi kesalahan prediksi positif, dan mendukung implementasi kebijakan pengelolaan lingkungan yang lebih efisien.           
                    ''')
            
    with st.expander("Kesimpulan"):
        st.caption('''- Dataset terdiri dari 29531 entris dan 16 kolom. Namun setelah dilakukan handling missing value, jumlah dataset yang digunakan yaitu 10823 entries dan 13 kolom.

- Terdapat dua kategori pada target 'AQI_Bucket' yaitu 'Good' dan 'Poor'. Kategori Good diganti menjadi 1 dan kategori Poor diganti menjadi 0.

- Pada data train dipilih bebera kolom sebagai feature. Pemilihan feature menggunakan uji Pearson, Kendall, Cardinality dan Multicolinear (VIF). Adapun hasil feature selection adalah 'PM2.5', 'NO', 'NO2', 'CO', 'SO2'.

- Digunakan metrics precision dengan alasan ingin mengukur seberapa akurat model dapat memprediksi kondisi udara yang sebenarnya buruk (poor) tapi terprediksi baik (good).

- Model RandomForestRegressor memberikan kinerja yang baik dalam memprediksi kualitas udara kota-kota di India. Model RandomForestRegressor memberikan hasil precision sebesar 93% pada data train dan 89% pada data test untuk prediksi target 'Good'. Sedangkan hasil precision sebesar 90% pada data train dan 91% pada data test untuk prediksi target 'Poor'.           
                   ''')



elif page == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()