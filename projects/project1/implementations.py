import numpy as np
import matplotlib.pyplot as plt 
from helpers import *

def mean_squared_error_gd(y, tx, initial_w, max_iters, gamma):
    # Linear regression using gradient descent
    N = len(y)
    w = initial_w
    for i in range(max_iters):
        e = y - tx @ w
        w -= gamma * (-1/N * (tx.T @ e))
    loss = MSE(y, tx, w)
    return w, loss

def mean_squared_error_sgd(y, tx, initial_w, max_iters, gamma):
    batch_size = 1
    # Shouldn't we have have a batch_size argument instead ? 
    N = len(y)
    w = initial_w
    for n_iter in range(max_iters):
        for minibatch_y, minibatch_tx in batch_iter(y, tx, batch_size):
            minibatch_e = minibatch_y - minibatch_tx @ w
            stoch_grad = -1/len(minibatch_y) * (minibatch_tx.T @ minibatch_e)
            # Update w
            w = w - gamma * stoch_grad
    loss = MSE(y, tx, w)
    return w, loss

def least_squares(y, tx):
    w = np.linalg.solve(tx.T @ tx, tx.T @ y)
    loss = MSE(y, tx, w)
    return w, loss

def ridge_regression(y, tx, lambda_):
    N = len(y)
    w = np.linalg.solve(tx.T @ tx + lambda_ * (2 * N) * np.identity(tx.shape[1]), tx.T @ y)
    loss = MSE(y, tx, w)
    return w, loss

def logistic_regression(y, tx, initial_w, max_iters, gamma):
    w = initial_w
    for i in range(max_iters):
        w -= gamma * log_loss_grad(y, tx, w)
    loss = log_loss(y, tx, w)
    return w, loss

def reg_logistic_regression(y, tx, lambda_, initial_w, max_iters, gamma):
    N = len(y)
    w = initial_w
    for i in range(max_iters):
        print(np.shape(log_loss_grad(y, tx, w)))
        print(np.shape(w))
        w -= gamma * (log_loss_grad(y, tx, w) + lambda_ * 2 * w)
    loss = log_loss(y, tx, w)
    return w, loss




# MAIN
w = np.array([[0.5], [1.0]])
tx = np.array([[2.3, 3.2], [1.0, 0.1], [1.4, 2.3]])
y = np.array([[0.1], [0.3], [0.5]])
y = (y > 0.2) * 1.0 # For the logistic regressions
max_iters = 2
gamma = 0.1
lambda_ = 1.0
#print(mean_squared_error_gd(y, tx, w, max_iters, gamma))
#print(mean_squared_error_sgd(y[:1], tx[:1], w, max_iters, gamma))
#print(least_squares(y, tx))
#print(ridge_regression(y, tx, lambda_))
#print(logistic_regression(y, tx, w, max_iters, gamma))
print(reg_logistic_regression(y, tx, lambda_, w, max_iters, gamma))