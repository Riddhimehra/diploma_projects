# Heart Disease Prediction Using Machine Learning

## 📌 About the Project

This project focuses on predicting whether a person is likely to have **heart disease** using Machine Learning techniques.

The project analyzes patient health-related information such as age, cholesterol level, blood pressure, chest pain type, maximum heart rate, and other medical parameters.

Two Machine Learning classification models are implemented:

* **Logistic Regression**
* **Random Forest Classifier**

After comparing both models, **Logistic Regression** achieved the higher accuracy and was selected as the best-performing model for this dataset.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## 📂 Dataset

The project uses a dataset named **`heart.csv`**.

The dataset contains 14 columns, including:

* Age
* Sex
* Chest Pain (`cp`)
* Resting Blood Pressure (`trestbps`)
* Cholesterol (`chol`)
* Fasting Blood Sugar (`fbs`)
* Resting ECG (`restecg`)
* Maximum Heart Rate (`thalach`)
* Exercise-Induced Angina (`exang`)
* Oldpeak
* Slope
* Number of Major Vessels (`ca`)
* Thalassemia (`thal`)
* Target

The `target` column represents the prediction:

* `0` = No Heart Disease
* `1` = Heart Disease

## 🔄 Project Workflow

1. Import required libraries
2. Load the heart disease dataset
3. Check dataset information
4. Check missing values
5. Remove duplicate records
6. Perform Exploratory Data Analysis (EDA)
7. Analyze correlations using a heatmap
8. Split data into training and testing sets
9. Apply feature scaling using StandardScaler
10. Train Logistic Regression
11. Train Random Forest Classifier
12. Compare model accuracy
13. Analyze feature importance
14. Select the best-performing model

## 📊 Data Preprocessing

The dataset is checked for missing values and duplicate rows. The original dataset contains **1025 rows**, with **723 duplicate rows** removed, leaving **302 records** for analysis.

The features are divided into:

* `X` → Input features
* `y` → Target variable

The data is split into training and testing sets using an **80:20 ratio**. StandardScaler is then used to scale the training and testing features for Logistic Regression.

## 📈 Exploratory Data Analysis

EDA is performed using:

* Dataset statistics
* Target distribution
* Correlation heatmap
* Feature correlation analysis

The correlation analysis identifies features that have stronger relationships with the target. The highest correlations shown in the project include `exang`, `cp`, `oldpeak`, `thalach`, and `ca`.

## 🤖 Machine Learning Models

### 1. Logistic Regression

Logistic Regression is trained using the scaled training data.

**Accuracy: 80.33%**

The classification report and confusion matrix are also generated to evaluate the model.

### 2. Random Forest Classifier

A Random Forest Classifier with **100 estimators** is trained on the training data.

**Accuracy: 75.41%**

A classification report and confusion matrix are generated for further evaluation.

## 🏆 Model Comparison

| Model               |   Accuracy |
| ------------------- | ---------: |
| Logistic Regression | **80.33%** |
| Random Forest       | **75.41%** |

Based on the accuracy comparison, **Logistic Regression is the best-performing model** in this project.

## 🔍 Feature Importance

Random Forest feature importance is used to understand which features contribute most to the model's predictions.

The feature-importance graph shows **`cp` (chest pain type)** as the most important feature, followed by `thalach`, `ca`, `oldpeak`, and `thal`.

## 📁 Suggested Project Structure

```text
Heart-Disease-Prediction/
│
├── heart_disease_prediction.ipynb
├── heart.csv
└── README.md
```

## 👩‍💻 Project Members

* **Riddhi Mehra**
* **Hetanshi Sodha**

**Subject:** Introduction to Machine Learning (IML)
**Subject Code:** 4350702

## ⚠️ Disclaimer

This project is an educational Machine Learning project. Its predictions should **not be treated as a medical diagnosis** or a replacement for professional medical advice.

## ✅ Conclusion

The project successfully demonstrates how Machine Learning can be used to analyze health-related data and predict the possibility of heart disease. Among the two tested models, **Logistic Regression performed better with an accuracy of 80.33%** and was selected as the best-performing model for this dataset.
