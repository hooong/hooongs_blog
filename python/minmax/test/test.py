import numpy as np

Xs = [12, 34, 55, 1, 100]

# min과 max를 구하는 과정
X = np.array(Xs)
X_min = X.min()
X_max = X.max()
X_denom = X_max - X_min

for i in range(len(X)):
  X[i] = (X[i] - X_min) // X_denom

print(X)