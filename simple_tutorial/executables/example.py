import tensorflow as tf
import numpy as np
from trainers.example import train
from data_loader.example import load
from models.example import build_model
from preprocessors.example import preprocess


### Here is the base template, you can use whichever loader, preprocessors, etc. 
### you wish to use.

def main():
	path = './data/data.csv'
	x, y = load(path)
	x, y = preprocess(x, y) #Optional
	model = build_model()
	history, results = train(model, x, y)
	history.to_csv('./results/histroy_example.csv', index=False)
	results.to_csv('./results/results_example.csv', index=False)

if __name__ == "__main__":
	main()
