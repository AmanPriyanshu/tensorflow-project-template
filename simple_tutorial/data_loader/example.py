import pandas as pd
import numpy as np

### Do not duplicate or change the name of the function
### load(), and return x and y, make sure even if y 
### is 1D array, convert it into a 2D one. Both should 
### ideally be numpy arrays

def load(path):
	data = pd.read_csv(path)
	data = data.values
	x = data.T[:-1].T
	y = data.T[-1]
	return x, y
