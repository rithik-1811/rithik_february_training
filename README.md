# Supervised Machine Learning – Regression Models

## Project Title

House Price Prediction using Supervised Machine Learning

---

## Problem Statement

Predicting house prices is an important task in real estate analysis.
This project builds machine learning models that predict house prices based on different property features such as size, number of bedrooms, house age, and distance from the city.

The goal is to apply supervised machine learning algorithms and compare their performance.

---

## Dataset Description

The dataset contains **1200 records** of houses with the following features:

| Feature          | Description                      |
| ---------------- | -------------------------------- |
| Size_sqft        | Size of the house in square feet |
| Bedrooms         | Number of bedrooms               |
| Bathrooms        | Number of bathrooms              |
| Age              | Age of the house                 |
| Distance_to_city | Distance from the city center    |
| Price            | Target variable – house price    |

The dataset is included in this repository inside the **dataset folder**.

---

## Data Preprocessing Steps

Before applying machine learning models, several preprocessing steps were performed:

1. **Handling Missing Values**
   Checked using `isnull()` to ensure the dataset has no missing entries.

2. **Removing Duplicate Records**
   Duplicate rows were removed using `drop_duplicates()`.

3. **Checking Data Types**
   Ensured that all numerical features were correctly formatted.

4. **Feature Selection**
   Selected relevant features that influence house price.

5. **Feature Scaling**
   Applied `StandardScaler` to normalize the feature values.

6. **Train-Test Split**
   Dataset was divided into:

   * 80% Training Data
   * 20% Testing Data

---

## Machine Learning Algorithms Used

Three supervised learning algorithms were implemented:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

These models were trained on the dataset and their performance was compared.

---

## Evaluation Metrics

The models were evaluated using the following regression metrics:

* **R² Score**
* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**
* **Mean Absolute Error (MAE)**

These metrics help determine how accurately the models predict house prices.

---

## Results and Observations

After training and testing the models:

* Linear Regression provided a good baseline prediction.
* Decision Tree captured nonlinear relationships in the data.
* Random Forest produced the best performance due to ensemble learning.

Random Forest generally provided the most accurate predictions.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn


## Conclusion

This project demonstrates how supervised machine learning algorithms can be used to solve regression problems such as house price prediction.

Data preprocessing plays a critical role in improving model performance.
Among the implemented algorithms, **Random Forest achieved the best results**, showing the strength of ensemble methods in regression tasks.



