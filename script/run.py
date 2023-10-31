import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from scipy.stats import kurtosis, skew
import numpy as np




df = pd.read_csv("../data/testing-dataset/vgsales.csv")
df = df.dropna(subset=['Year'])


num_rows_to_use = 200
columns_to_use = ['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
df = df.loc[:num_rows_to_use - 1, columns_to_use]


features = ['Year', 'NA_Sales']
X = df[features]
y = df['Global_Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)


print("Maximum Aptitude (Decision Tree):", np.max(dt_predictions))
print("Minimum Aptitude (Decision Tree):", np.min(dt_predictions))
print("Energy (Decision Tree):", np.sum(dt_predictions**2))
print("Skewness (Decision Tree):", skew(dt_predictions))
print("Kurtosis:", kurtosis(dt_predictions))
print("Medium Kurtosis (Decision Tree):", np.median(kurtosis(dt_predictions)))

print("------------------------------------------------")

knn_model = KNeighborsRegressor()
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)

print("Maximum Aptitude (KNN):", np.max(knn_predictions))
print("Minimum Aptitude (KNN):", np.min(knn_predictions))
print("Energy (KNN):", np.sum(knn_predictions**2))
print("Skewness (KNN):", skew(knn_predictions))
print("Kurtosis:", kurtosis(knn_predictions))
print("Medium Kurtosis (KNN):", np.median(kurtosis(knn_predictions)))


print("----------------other matrics---------------- ")

print("Decision Tree Metrics:")
print("MAE:", mean_absolute_error(y_test, dt_predictions))
print("MSE:", mean_squared_error(y_test, dt_predictions))
print("R-squared:", r2_score(y_test, dt_predictions))

print("\nKNN Metrics:")
print("MAE:", mean_absolute_error(y_test, knn_predictions))
print("MSE:", mean_squared_error(y_test, knn_predictions))
print("R-squared:", r2_score(y_test, knn_predictions))
