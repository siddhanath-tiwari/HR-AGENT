# Model training script phase 2nd

import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Simulated Resume Features & Labels (1: Selected, 0: Rejected)
X = np.random.rand(100, 10)
y = np.random.choice([0, 1], size=100)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

pickle.dump(model, open("models/resume_model.pkl", "wb"))
print("Model trained successfully!")