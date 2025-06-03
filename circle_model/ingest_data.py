from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

def main():
    # Make 1000 samples 
    n_samples = 1000

    # Create circles
    X, y = make_circles(n_samples,
                        noise=0.03, # a little bit of noise to the dots
                        random_state=42) # keep random state so we get the same values
    #y has a binary label for each circle that is attached to the coordinate (X1,X2) 
    #At the moment there is a shape mismatch between X and y and X is a 2d vector while y is 1d
    # View the first example of features and labels
    X_sample = X[0]
    y_sample = y[0]
  
    # Turn data into tensors
    # Otherwise this causes issues with computations later on
    import torch
    X = torch.from_numpy(X).type(torch.float)
    y = torch.from_numpy(y).type(torch.float)

    # Split data into train and test sets

    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=0.2, # 20% test, 80% train
                                                        random_state=42) # make the random split reproducible

    # print(len(X_train), len(X_test), len(y_train), len(y_test)): 800 200 800 200
    return X_train, X_test, y_train, y_test
