# Disease Model Prediction Project

## Project Overview

This repository contains a disease prediction model that allows users to input body health metrics data and receive predictions about potential diseases. The project includes two models that can be tested and deployed locally or accessed via a Streamlit deployment.

## Getting Started

To start the deployment on this project, follow the instructions below:

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

Or..... you can just access the deployed Streamlit application from this link:
[Streamlit Model Deployment](https://capstone-c242-ps384-deploy-model.streamlit.app/)

## Testing the Model Code

### Model 1: Health Data Prediction

Before the setup, make sure you are inside "Capstone-2C24-PS384_Project01" as the root folder in the code editor.

1. **Set Up the Environment**
   - Make sure you are using a conda environment with Python 3.10.15.
   - Install the required packages by running:
     ```bash
     pip install -r scripts/requirement-model1.txt
     ```
   - Run the import cell section to test the installed library, make sure there is no error

2. **Check Data Availability**
   - Make sure all required dataset files are present in the `dataset/health_data1` folder.
   - If there any files are missing, you will see a error message indicating which files are not found when running the next step.

3. **Preprocess the dataset**
   - Run the cell with the preprocessing code to combined the dataset.
   - Once data preprocessing is done, the new dataset will be saved in the 'dataset/health_data1' folder as 'combined_dataset.csv'

4. **Train the Model**
   - After all data is loaded, the model will be trained. Pay attention to the output to see accuracy and other metrics.

5. **Save the Model**
   - Once training is complete, the model will be saved in the `models` folder as an HDF5 file.

### Model 2: Symptoms Prediction

1. **Set Up the Environment**
   - Ensure you are using a conda environment with Python 3.10.15.
   - If you have already installed the requirements for Model 1, you do not need to install them again for Model 2.

2. **Input Symptoms**
   - At the end of the notebook, you can input symptoms in Indonesian according to what is listed in `symptoms_mapping`.

3. **View Predictions**
   - After running the appropriate cell, you will see disease predictions based on the input symptoms.

### Convert HDF5 to TFJS

1. **Set Up the Environment**
   - Make sure you are using the virtual environment `tfjs-env`.

2. **Run**
   - Run the specific cell to perform a model conversion