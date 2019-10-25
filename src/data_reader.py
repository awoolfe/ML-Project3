import numpy as np

'''
Loads the data set into a numpy array
The shape is (50_000, 128, 128)
'''
data = np.load('../data/train_max_x', allow_pickle=True)
