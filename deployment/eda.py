import streamlit as st
from PIL import Image

def run():
    st.title('Welcome to EDA')


    st.subheader('Perbandingan Kualitas Udara Antar Kota di India')
    image = Image.open('perbandingan kualitas udara.png')
    st.image(image, caption='figure 1')

    with st.expander('Explanation'):
        st.caption('Berdasarkan nilai Air Quality Index (AQI), kota dengan kualitas udara yang paling buruk yaitu Ahmedabad dan kota dengan kualitas udara paling bagus yaitu Aizawl. Adapun urutan 5 kota dengan kualitas udara terbaik yaitu Aizawl, Shillong, Coimbatore, Thiruvananthapuram, dan Ernakulam. Untuk urutan 5 kota dengan kualitas udara terburuk yaitu Ahmedabad, Delhi, Patna, Gurugram, dan Lucknow.')


    st.subheader('Parameter PM2.5 Dari Waktu ke Waktu')
    image = Image.open('pm25.png')
    st.image(image, caption='figure 2')

    with st.expander('Explanation'):
        st.caption('Parameter PM2.5 memiliki pergerakan yang stabil dengan trend stationary dari tahun ke tahun.')


    st.subheader('Korelasi Antar Parameter Pencemaran Udara')
    image = Image.open('corr variables.png')
    st.image(image, caption='figure 3')

    with st.expander('Explanation'):
        st.caption('Dari gambar heatmap di atas diketahui bahwa Toluene dan Benzene memiliki korelasi antar parameter pencemar udara yang cukup tinggi yaitu sebesar 0.74, sedangkan pada Benzene dan O3 memiliki korelasi antar parameter pencemar udara yang sangat kecil yaitu 0.02.')

    st.subheader('Perubahan Kualitas Udara Seiring Waktu')
    image = Image.open('kualitas udara thn ke thn.png')
    st.image(image, caption='figure 5')

    with st.expander('Explanation'):
        st.caption('Pada tahun 2015 kualitas udara di India sempat menjadi yang paling buruk diantara tahun lainnya, dan pada tahun 2015 juga terjadi kenaikan kualitas udara yang signifikan.')

    st.subheader('Persentase Parameter CO Terhadap Target')
    image = Image.open('param co x target.png')
    st.image(image, caption='figure 4')

    with st.expander('Explanation'):
        st.caption('Pada kategori Poor parameter CO memiliki rata-rata paling tinggi yaitu sebesar 6.80062 dan pada kategori Good memiliki rata-rata sebesar 1.23447.')

    st.subheader('Proporsi Data Target AQI_Bucket')
    image = Image.open('target.png')
    st.image(image, caption='figure 4')

    with st.expander('Explanation'):
        st.caption('Proporsi target "Good" lebih banyak daripada target "Poor". Jumlah target "Good" sebanyak 5.956 dan target "Poor" sebanyak 4.867.')

if __name__ == "__name__":
     run()
