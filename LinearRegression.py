import numpy as np

# Data
dataX = np.array([6, 12, 14, 6, 9, 13, 15, 9])
dataY = np.array([300, 400, 560, 250, 290, 650, 630, 520])
X = 15

# Calculate averages
dataXAvg = np.mean(dataX)
dataYAvg = np.mean(dataY)

# Deviation from the mean
x = dataX - dataXAvg
y = dataY - dataYAvg

# Calculate products and squares
xy = x * y
xSqr = x ** 2
ySqr = y ** 2

# Summations
sumxy = np.sum(xy)
sumxSqr = np.sum(xSqr)
sumySqr = np.sum(ySqr)

# Correlation coefficient
rCoefficient = sumxy / np.sqrt(sumxSqr * sumySqr)

# Regression coefficients
b = sumxy / sumxSqr
a = dataYAvg - b * dataXAvg

# Predict Y for given X
Y = a + b * X

# Output results
print("Correlation Coefficient (r):", rCoefficient)
print("Intercept (a):", a)
print("Slope (b):", b)
print("Predicted Y for X =", X, ":", Y)
