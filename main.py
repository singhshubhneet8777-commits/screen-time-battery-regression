"""
Screen Time vs Battery Usage
A beginner-friendly Linear Regression project using sample data.
"""

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Sample data: screen time in minutes and battery used in percentage points.
screen_time = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]
battery_used = [3, 6, 9, 13, 16, 20, 23, 27, 30, 34]

# Scikit-learn expects X (input features) to be two-dimensional.
X = [[value] for value in screen_time]
y = battery_used

# Keep 20% of the observations for testing and use 80% for training.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model.
model = LinearRegression()
model.fit(X_train, y_train)

# Predict battery usage for the held-out test examples.
y_pred = model.predict(X_test)

print("Test screen times:", [row[0] for row in X_test])
print("Predicted battery use (%):", y_pred.round(2))
print("Actual battery use (%):", y_test)
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred):.2f}")

# Plot the observations and the fitted regression line.
# Sorting the x-values keeps the line connected in the correct order.
sorted_pairs = sorted(zip(screen_time, battery_used))
x_sorted = [pair[0] for pair in sorted_pairs]
X_sorted = [[value] for value in x_sorted]

plt.scatter(screen_time, battery_used, label="Sample data")
plt.plot(x_sorted, model.predict(X_sorted), color="tomato",
         label="Linear regression prediction")
plt.xlabel("Screen time (minutes)")
plt.ylabel("Battery used (%)")
plt.title("Screen Time vs Battery Usage")
plt.legend()
plt.tight_layout()
plt.show()
