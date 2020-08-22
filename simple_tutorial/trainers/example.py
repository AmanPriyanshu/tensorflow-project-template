import pandas as pd
import tensorflow as tf

### Do not duplicate or change the name of the function
### train, you can choose to include callbacks, save checkpoints 
### and return basic results as results and the history (we are 
### converting it to a pandas DataFrame before sending) of the model.

def train(model, x, y):

	history = model.fit(x, y, epochs=25, validation_split=0.1, shuffle=True)
	results = model.evaluate(x, y)
	results = pd.DataFrame({'loss':[results[0]], 'acc': [results[1]]})
	history = pd.DataFrame(history.history)
	return history, results
