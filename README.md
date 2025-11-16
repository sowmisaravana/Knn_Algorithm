# ⭐ K-Nearest Neighbors (KNN) Algorithm – Description

K-Nearest Neighbors (KNN) is a supervised machine learning algorithm used for both classification and regression, but it is most commonly used for classification tasks.
It is an instance-based, non-parametric, and lazy learning algorithm.

# 🔍 How KNN Works

Store all the training data.
KNN does not build a model; instead, it keeps the dataset as it is.

When a new data point comes, KNN:

Calculates the distance (usually Euclidean) between this point and all other points in the dataset.

Finds the k nearest neighbors (k is a chosen number like 3, 5, 7...).

Looks at the labels of these neighbors.

Prediction:

Classification: The class that appears the most among the neighbors is selected (majority vote).

Regression: The average of the neighbors' values is taken.

# 🧠 Why It’s Called “Lazy Learning”

KNN does not learn a model during training.
There is no training phase — computation happens only during prediction.
This is why it's called a lazy learner.

# 📏 Common Distance Metrics

Euclidean distance (most common)

Manhattan distance

Minkowski distance

Hamming distance (for categorical data)

# ⚙️ Choosing K

Small k → more sensitive to noise

Large k → smoother decision boundary but may oversimplify

Usually, an odd value of k is chosen for classification.

# ✅ Advantages

Simple and easy to understand

No need to build a model

Works well with small datasets

Naturally handles multi-class classification

# ❌ Disadvantages

Slow for large datasets (because it checks distance to every point)

Sensitive to irrelevant features

Requires scaling (StandardScaler)

Performance depends heavily on choosing the right k

# 🎯 Where KNN Is Used

Recommender systems

Image classification

Fraud detection

Pattern recognition

Predictive analytics
# screenshort
<img width="962" height="727" alt="Screenshot 2025-11-16 235429" src="https://github.com/user-attachments/assets/a0b26fb8-26fb-4deb-8433-eca052891637" />
