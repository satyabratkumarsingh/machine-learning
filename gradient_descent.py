
import numpy as np

def gradient_descent(x, y): 
    w_curr = b_curr = 0
    iterations = 10000
    size_n = len(x)
    learning_rate = 0.09

    for i in range(iterations): 
        y_predicted = w_curr* x  + b_curr
        cost = (1/size_n) * sum([ val ** 2 for val in (y - y_predicted)])
        w_derivative = (1/size_n) * sum( x* (y_predicted - y))
        b_derivative = (1/size_n) * sum(y_predicted - y)
        w_curr = w_curr - learning_rate * w_derivative
        b_curr = b_curr - learning_rate * b_derivative
        print("iteration: {}, w : {} , b: {} , Cost {} ".format(i, w_curr, b_curr, cost))

x = np.array([1,2,3,4,5])
y = np.array([10,20,30,40,50])

gradient_descent(x, y)
