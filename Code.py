# Import libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Load dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Function to evaluate model
def evaluate_model(model, name):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"{name} Results:")
    print(f"MSE: {mse}")
    print(f"R2 Score: {r2}")
    print("-" * 30)

    return mse, r2

# Models
lr = LinearRegression()
dt = DecisionTreeRegressor()
rf = RandomForestRegressor()

# Evaluate all models
results = {}

results["Linear Regression"] = evaluate_model(lr, "Linear Regression")
results["Decision Tree"] = evaluate_model(dt, "Decision Tree")
results["Random Forest"] = evaluate_model(rf, "Random Forest")