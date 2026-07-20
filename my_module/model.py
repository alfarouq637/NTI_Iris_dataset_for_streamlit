import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)


def predict(petal_width, petal_length, sepal_width, sepal_length):
    # Make a prediction based on the input features
    input_features = np.array(
        [[petal_width, petal_length, sepal_width, sepal_length]]
    )
    prediction = clf.predict(input_features)

    # Return the predicted species name
    return iris.target_names[prediction][0]