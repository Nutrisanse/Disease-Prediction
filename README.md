# Disease Model Prediction Project

## Project Overview

This repository contains a disease prediction model that allows users to input health data and receive predictions about potential diseases. The project includes two models that can be tested and deployed locally or accessed via a Streamlit deployment.

## Getting Started

To get started with this project, follow the instructions below:

### Clone the Repository

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/dana-ml27-bangkit2024/Capstone-C242-PS384_Project01
   cd Capstone-C242-PS384_Project01
   ```

### Testing Model Deployment

#### Model 1

To test the deployment of Model 1, follow these steps:

1. Navigate to the `models` directory.
2. Start a local HTTP server:
   ```bash
   python -m http.server
   ```
3. Open Google Chrome and enter the following URL:
   ```
   http://localhost:8000/models/index1.html
   ```

#### Model 2

To test the deployment of Model 2, follow these steps:

1. Navigate to the `models` directory.
2. Start a local HTTP server:
   ```bash
   python -m http.server
   ```
3. Open Google Chrome and enter the following URL:
   ```
   http://localhost:8000/models/index2.html
   ```

### Running the Streamlit Application

To run the Streamlit application locally:

1. Ensure you are in the root folder of the project.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

Alternatively, you can access the deployed Streamlit application using the following link:
[Streamlit Deployment](https://capstone-c242-ps384-deploy-model.streamlit.app/)

## Testing the Model Code

### Model 1: Health Data Prediction

1. **Set Up the Environment**
   - Pastikan Anda menggunakan environment conda dengan Python 3.10.15.
   - Install requirements yang diperlukan dengan menjalankan:
     ```bash
     pip install -r scripts/requirement-model1.txt
     ```

2. **Run the Jupyter Notebook**
   - Buka terminal dan navigasikan ke direktori `scripts`:
     ```bash
     cd scripts
     ```
   - Jalankan Jupyter Notebook:
     ```bash
     jupyter notebook health_data1_tf.ipynb
     ```
   - Setelah Jupyter Notebook terbuka di browser, jalankan setiap sel secara berurutan untuk memproses data dan melatih model.

3. **Check Data Availability**
   - Pastikan semua file dataset yang diperlukan ada di folder `dataset/health_data1`.
   - Jika ada file yang hilang, Anda akan melihat pesan yang menunjukkan file yang tidak ditemukan.

4. **Train the Model**
   - Setelah semua data dimuat, model akan dilatih. Perhatikan output untuk melihat akurasi dan metrik lainnya.

5. **Save the Model**
   - Setelah pelatihan selesai, model akan disimpan di folder `models` sebagai file HDF5.

### Model 2: Symptoms Prediction

1. **Set Up the Environment**
   - Pastikan Anda menggunakan environment conda dengan Python 3.10.15.
   - Jika Anda sudah menginstal requirements untuk Model 1, Anda tidak perlu menginstalnya lagi untuk Model 2.

2. **Run the Jupyter Notebook**
   - Buka terminal dan navigasikan ke direktori `scripts`:
     ```bash
     cd scripts
     ```
   - Jalankan Jupyter Notebook:
     ```bash
     jupyter notebook symptoms-predict.ipynb
     ```
   - Setelah Jupyter Notebook terbuka di browser, jalankan setiap sel secara berurutan untuk memproses data dan membuat prediksi berdasarkan gejala yang dimasukkan.

3. **Input Symptoms**
   - Di bagian akhir notebook, Anda dapat memasukkan gejala dalam bahasa Indonesia sesuai dengan yang terdaftar di `symptoms_mapping`.

4. **View Predictions**
   - Setelah menjalankan sel yang sesuai, Anda akan melihat prediksi penyakit berdasarkan gejala yang dimasukkan.

### Convert HDF5 to TFJS

1. **Set Up the Environment**
   - Pastikan Anda menggunakan virtual environment `tfjs-env`.

2. **Run the Jupyter Notebook**
   - Buka terminal dan navigasikan ke direktori `scripts`:
     ```bash
     cd scripts
     ```
   - Jalankan Jupyter Notebook:
     ```bash
     jupyter notebook tfjs-converter.ipynb
     ```
   - Ikuti instruksi di dalam notebook untuk mengonversi model HDF5 ke format TFJS.

## Conclusion

By following the instructions above, you will be able to test and deploy the disease prediction models. If you have any questions or need further assistance, feel free to reach out!