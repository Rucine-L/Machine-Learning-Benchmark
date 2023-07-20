import numpy as np
from model.Model import Model
from model.CARTDecisionTree import CARTDecisionTree
from sklearn.datasets import load_iris,load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error

class RandomForest(Model):
    def __init__(self, learning_rate=1.0, n_trees=10):
        self.learning_rate = learning_rate
        self.n_trees = n_trees
        self.trees = []

    def train(self, X_train, y_train):
        for _ in range(self.n_trees):
            tree = CARTDecisionTree(learning_rate=self.learning_rate)
            tree.train(X_train, y_train)
            self.trees.append(tree)

    def predict(self, X_test):
        #X_test=X_test.values
        predictions = np.zeros(len(X_test))
        for tree in self.trees:
            predictions += self.learning_rate * tree.predict(X_test)
        return np.round(predictions / len(self.trees))

