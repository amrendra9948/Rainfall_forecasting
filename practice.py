# import numpy as np
# import pickle
# import streamlit as st

# loaded_model = pickle.load(open('C:/Users/Harsh Singh/OneDrive/Documents/Jupyer/trained_model.sav', 'rb'))

# # create a function for prediction

# def heart_prediction(input_data):

#     input_data_as_numpy_array= np.asarray(input_data)
#     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#     prediction = loaded_model.predict(input_data_reshaped)
#     print(prediction)

#     if(prediction[0]==0):
#       return 'The persion does not have a heart disease'
#     else:
#       return 'The persion have a heart disease'


# def main():

#     st.title('Heart disease prediction')

#     #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal

#     age= st.text_input('Enter your age')
#     sex= st.text_input('Enter your sex')
#     cp= st.text_input('Enter your cp')
#     trestbps= st.text_input('Enter your trestbps')
#     chol= st.text_input('Enter your chol')
#     fbs= st.text_input('Enter your fbs')
#     restecg= st.text_input('Enter your restecg')
#     thalach= st.text_input('Enter your thalach')
#     exang= st.text_input('Enter your exang')
#     oldpeak= st.text_input('Enter your oldpeak')
#     slope= st.text_input('Enter your slope')
#     ca= st.text_input('Enter your ca')
#     thal= st.text_input('Enter your thal')

#     #code for prediction
#     diagnosis=''

#     if st.button("Heart test result"):
#        diagnosis = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])

#     st.success(diagnosis)


# if __name__ == '__main__':
#     main()




# #  streamlit run "c:\Users\Harsh Singh\OneDrive\Documents\Jupyer\webpage.py" for RUNNING