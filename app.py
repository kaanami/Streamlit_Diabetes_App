import streamlit as st
import numpy as np

from diabetes import predict_diabetes

st.title('Diabetes Prediction App')

st.header('Enter your data: ')
glucose = st.number_input('Glucose', 0,400)
# dfp = st.number_input('DFP', 0,15)
age = st.number_input('Age', 0,100)

if st.button('Predict'):
    to_predict = np.array([[glucose, age]])  # dfp

    result = predict_diabetes(to_predict)
    print(result)

    if result[0] == 0:
        st.success('Congratulation! No chance of Diabetes.')
    else:
        st.warning('Chance of Diabetes, please visit your doctor asap!!')


