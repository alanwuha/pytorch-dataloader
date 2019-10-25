import numpy as np

class NearestNeighbor:
    def __init__(self):
        pass

    def train(self, X, y):
        """" X is N x D where each row is an example. Y is 1-dimension of size N """
        self.Xtr = X
        self.ytr = y

    def predict(self, X):
        """ X is N x D where each row is an example we wish to predict label for """
        num_test = X.shape[0]
        # let's make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype = self.ytr.dtype)

        # loop over all test rows
        for i in np.xrange(num_test):
            # find the nearest training image to the i'th test image
            # using the L1 distance (sum of absolute value difference)
            distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)
            min_index = np.argmin(distances) # get the index with smallest distance
            Ypred[i] = self.ytr(min_index) # predict the label of the nearest example

        return Ypred