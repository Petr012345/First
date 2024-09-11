import numpy as np


class Linear_model:
    def __init__(self, l):
        self.W = np.zeros(l)
        # self.W = None

    def gradient_descent(self, X, Y, alf):
        w_delta = (2/X.shape[1])*(X.T.dot(X.dot(self.W.T)-Y))
        self.W -= alf*w_delta

    def loss_func(self, Y, P_Y):
        return np.sum(np.square(Y-P_Y))

    def formulated_fit(self, X, Y, lam=0.0):
        reg_matrix = lam * np.eye(X.shape[1], X.shape[1])
        self.W = np.dot(np.linalg.inv(np.dot(X.T, X)+reg_matrix),np.dot(X.T, Y))

    def predict(self, X):
        return np.dot(X, self.W.T)
