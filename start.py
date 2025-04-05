import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/91639/Desktop/final/trained_model.sav', 'rb'))

input_data = (1015.9, 19.9, 95, 81, 0.0, 40.0, 11.5)
input_data_as_numpy_array= np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
    print('No Rainfall')
else:
    print('Rainfall')