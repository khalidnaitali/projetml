# 🫀 Cardiac Risk Prediction Dashboard

🔗 **Application en ligne** :
[https://projetml-ehdcul93spjgcrnycmvs84.streamlit.app/](https://projetml-ehdcul93spjgcrnycmvs84.streamlit.app/)

---

## 📌 Project Overview

This project presents a **Machine Learning–based dashboard** for predicting the **risk of coronary heart disease (CHD)** using clinical and lifestyle data.
The application is built with **Python**, **scikit-learn**, and **Streamlit**, and follows a complete end-to-end Machine Learning workflow.

The goal is to demonstrate how predictive models can be trained, evaluated, and deployed in an interactive web application.

---

## 🎯 Objectives

* Perform exploratory data analysis on the CHD dataset
* Build robust preprocessing pipelines for numerical and categorical data
* Apply dimensionality reduction using **PCA**
* Train and compare multiple supervised learning models
* Handle class imbalance using **SMOTE**
* Select and save the best-performing model
* Deploy the final model in a **Streamlit dashboard**

---

## 📊 Dataset

The project uses the **CHD (Coronary Heart Disease)** dataset, which contains patient-level clinical and behavioral data.

### Input Features

* Systolic blood pressure (SBP)
* Tobacco consumption
* LDL cholesterol
* Adiposity
* Type A behavior
* Obesity
* Alcohol consumption
* Age
* Family history of heart disease (`famhist`)

### Target Variable

* `chd`

  * `0` → No heart disease
  * `1` → Presence of heart disease

---

## ⚙️ Machine Learning Pipeline

The project is implemented using **scikit-learn Pipelines**, ensuring reproducibility and preventing data leakage.

### Main steps:

1. **Data preprocessing**

   * Missing value imputation
   * Standardization of numerical features
   * One-Hot Encoding of categorical variables
2. **Dimensionality reduction**

   * Principal Component Analysis (PCA) with 90% explained variance
3. **Modeling**

   * Logistic Regression (with and without PCA)
   * K-Nearest Neighbors (KNN)
4. **Class imbalance handling**

   * SMOTE (Synthetic Minority Over-sampling Technique)
5. **Hyperparameter optimization**

   * GridSearchCV
6. **Model selection and serialization**

   * Final model saved as `Model.pkl`

---

## 🖥️ Streamlit Dashboard

The deployed application allows users to:

* Enter patient clinical information
* Run real-time predictions
* View:

  * Predicted cardiac risk (High / Low)
  * Estimated probability of heart disease

The interface is designed as a **minimal admin-style dashboard**, focusing on clarity, usability, and stability.

---

## 🚀 Deployment

The application is deployed using **Streamlit Cloud**.

🔗 **Live App**:
[https://projetml-ehdcul93spjgcrnycmvs84.streamlit.app/](https://projetml-ehdcul93spjgcrnycmvs84.streamlit.app/)

---

## 🛠️ Technologies Used

* Python 3
* pandas, numpy
* scikit-learn
* imbalanced-learn
* joblib
* Streamlit

---

## 📁 Project Structure

```
├── train_model.py        # Model training and selection
├── app.py                # Streamlit application
├── CHD.csv               # Dataset
├── Model.pkl             # Trained model
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 📌 How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python train_model.py

# Launch the Streamlit app
streamlit run app.py
