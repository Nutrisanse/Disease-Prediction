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

## Conclusion

By following the instructions above, you will be able to test and deploy the disease prediction models. If you have any questions or need further assistance, feel free to reach out!