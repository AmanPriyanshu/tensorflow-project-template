import numpy as np

### Do not duplicate or change the name of the function
### preprocess and return x and y, make sure even if y 
### is 1D array, convert it into a 2D one Both should 
### ideally be numpy arrays

def preprocess(x, y):
	y_new = []
	for i in y:
		a = [0, 0, 0, 0]
		a[int(i)]=1
		y_new.append(a)	
	y = np.array(y_new)
	return x, y
