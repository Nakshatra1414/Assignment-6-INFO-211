# Assignment-6-INFO-211


# Diabetes Regression Analysis using Scikit-Learn

## 📌 Project Overview

This project applies machine learning regression techniques to the diabetes dataset provided by Scikit-Learn. The goal is to build and evaluate multiple regression models to predict disease progression based on various medical features.

## 📌 Purpose

The purpose of this project is to:

* Practice data preprocessing and model building in Python
* Apply regression techniques using Scikit-Learn
* Compare model performance using evaluation metrics
* Understand how different models perform on real-world data

## 📊 Dataset

The dataset used is the built-in **diabetes dataset** from Scikit-Learn. It contains:

* 10 baseline medical features (such as BMI, blood pressure, etc.)
* A target variable representing disease progression

## ⚙️ Models Implemented

The following regression models were used:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

## 🧠 Methodology

1. Imported the dataset using Scikit-Learn
2. Split the data into training (80%) and testing (20%) sets
3. Trained each model using the training data
4. Evaluated model performance using:

   * Mean Squared Error (MSE)
   * R² Score

## 📈 Results

| Model             | MSE     | R² Score |
| ----------------- | ------- | -------- |
| Linear Regression | 2900.19 | 0.4526   |
| Decision Tree     | 5410.38 | -0.0212  |
| Random Forest     | 3128.88 | 0.4094   |

## 🏆 Conclusion

Linear Regression performed the best among the three models, achieving the lowest Mean Squared Error and the highest R² score. This suggests that the dataset has a relatively linear relationship between features and the target variable.

The Decision Tree model performed poorly and showed signs of overfitting, while Random Forest performed reasonably well but did not outperform Linear Regression.

## ⚠️ Limitations

* No hyperparameter tuning was applied
* Limited dataset size
* No feature engineering or scaling performed

## 🔧 Future Improvements

* Tune model parameters (especially Random Forest)
* Apply feature selection or scaling
* Try additional models such as Gradient Boosting

## 💻 Technologies Used

* Python
* Scikit-Learn
* NumPy
* Pandas

## 📂 How to Run the Project

1. Clone the repository
2. Install required libraries:

   ```
   pip install scikit-learn pandas numpy
   ```
3. Run the Python script:

   ```
   python main.py
   ```

## 🤖 AI Usage

Generative AI (ChatGPT) was used to assist with understanding concepts, structuring code, and improving documentation. All code was reviewed and modified as needed.

---
