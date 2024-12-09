import pandas as pd
import streamlit as st
import pickle

# Load Model XGBoost
model_pred = pickle.load(open('./models/model.pkl', 'rb'))

# Judul dan Pendahuluan
st.title('Sistem Prediksi Status Mahasiswa Jaya Jaya Institut Berbasis Machine Learning Model XGBoost :sparkles:')
st.write(
    """
        Sistem prediksi dirancang untuk mampu menklasifikasikan data-data mahasiswa dengan Status 'Enrolled' untuk dapat mengetahui peluang kemungkinan Graduate atau Dropout.
        Sistem prediksi dibuat sederhana agar memudahkan pengguna dengan memasukkan data (upload data) dalam bentuk csv kemudian menekan button Prediksi maka akan muncul hasil prediksi Status mahasiswa.
        Contoh data yang dapat digunakan :
    """
)
st.markdown("[Dataset Sample](https://github.com/Abito21/Proyek_Analisis_Solusi_Performa_Mahasiswa/blob/main/dataset/data_predict_students.csv)")

# Bagian Sidebar Keterangan Creator
st.sidebar.header("Sistem Prediksi Status Mahasiswa Jaya Jaya Institut")
st.sidebar.subheader("Created By")
st.sidebar.write("Nama            : Abid Juliant Indraswara")
st.sidebar.markdown("Email Dicoding : [Email](https://www.dicoding.com/users/abidindraswara/academies).")
st.sidebar.markdown("ID Dicoding\t: [abidindraswara](https://www.dicoding.com/users/abidindraswara/academies).")

# Fungsi untuk mewarnai prediksi
def color_pred(val):
    color = 'red' if val == 'Dropout' else 'blue'
    return f'color: {color}'

# Upload File Format csv
upload_file = st.file_uploader("Upload File Format csv ", type=["csv"])

if upload_file is not None:
    # Assign ke Variabel data_pred
    data_pred = pd.read_csv(upload_file)
    
    # Remove kolom Status jika ada
    data_pred = data_pred.drop(columns=['Status'], errors='ignore')
    
    # Menampilkan 10 Data Teratas
    st.write(data_pred.head(10))
    
    # Button Prediksi
    if st.button('Prediksi'):
        # Lakukan Prediksi
        predictions = model_pred.predict(data_pred)
    
        # Menambahkan Kolom 'Predicted Status' yang berisi 'Graduated' atau 'Dropout'
        data_pred['Predicted Status'] = ['Graduated' if pred == 1 else 'Dropout' for pred in predictions]
    
        # Menampilkan Hasil Prediksi Status Mahasiswa
        st.write("Hasil Prediksi Status Mahasiswa :")
        st.dataframe(data_pred.style.applymap(color_pred, subset=['Predicted Status']))

st.caption('Copyright (C) Abid Indraswara 2024')