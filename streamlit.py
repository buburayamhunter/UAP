import streamlit as st
import tensorflow as tf
import numpy as np

# Tampilan judul dengan gaya
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>Klasifikasi Citra Anjing</h1>
    <h3 style='text-align: center;'>Unggah citra dan lihat hasil prediksi!</h3>
    """,
    unsafe_allow_html=True,
)

# Sidebar untuk mengunggah file
st.sidebar.title("Pengaturan")
upload = st.sidebar.file_uploader(
    'Unggah Citra Anjing Anda',
    type=['png', 'jpg', 'jpeg']
)

def predict(image_file):
    # Kategori kelas
    class_names = ["Normal", "Defect"]
    
    # Preproses gambar
    img = tf.keras.utils.load_img(image_file, target_size=(300, 400, 3))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    # Memuat model dan memprediksi
    model = tf.keras.models.load_model("vgg_model.h5")
    output = model.predict(img_array)
    print(output)
    score = tf.nn.softmax(output['class_output'][0])
    return class_names[np.argmax(score)], np.max(score)

def predict_cnn(image_file):
    # Kategori kelas
    class_names = ["Normal", "Defect"]
    
    # Preproses gambar
    img = tf.keras.utils.load_img(image_file, target_size=(300, 400, 3))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    # Memuat model dan memprediksi
    model = tf.keras.models.load_model("vgg_model.h5")
    output = model.predict(img_array)
    print(output)
    score = tf.nn.softmax(output['class_output'][0])
    return class_names[np.argmax(score)], np.max(score)

# Button untuk prediksi
if st.sidebar.button("Prediksi"):
    if upload is not None:
        # Tampilkan citra yang diunggah
        st.image(upload, caption="Citra yang diunggah", use_column_width=True)
        st.subheader("Hasil Prediksi:")
        
        with st.spinner('Memproses prediksi, harap tunggu...'):
            try:
                predicted_class, confidence = predict_cnn(upload)
                st.success(f"Prediksi CNN : **{predicted_class}** dengan tingkat keyakinan {confidence:.2%}")

                predicted_class, confidence = predict(upload)
                st.success(f"Prediksi VGG : **{predicted_class}** dengan tingkat keyakinan {confidence:.2%}")
            except Exception as e:
                st.error("Terjadi kesalahan saat memproses gambar. Pastikan file yang diunggah benar.")
                st.error(str(e))
    else:
        st.warning("Harap unggah file citra terlebih dahulu di sidebar.")

# Menambahkan catatan di footer
st.sidebar.markdown("---")
st.sidebar.info("Klasifikasi kerusakan kardus")
st.sidebar.markdown(
    """
    Repository : 
    [GitHub](https://github.com/buburayamhunter/UAP)
    """
)
