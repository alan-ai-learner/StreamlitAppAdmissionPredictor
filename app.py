import streamlit as st
import numpy as np
import sklearn
#Ml package
import pickle
def predict(data):
    model = open('finalized_model.pickle',"rb")
    final_model = pickle.load(model)
    result  = final_model.predict([data])
    return result


def main():
    """"Chance Of admission"""
    st.header("Admission Predictor ML App for admission chance predictor.")
    st.subheader("Create by Alankar Shukla.")
    html_temp = """
    <div style="background-color:tomato;padding:15px;">
    <h2>Streamlit ML App</h2>
    </div)  
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.header('Enter you details here:')
    Rating = st.slider(' 1. Rating of University is:',1,5)
    CGPA = st.slider(' 1.Your CGPA is is:',1.0,10.0)   
    GRE = st.number_input('2. Enter your GRE score:')
    TOEFL = st.number_input('2. Enter your TOEFL score:')
    SOP = st.number_input('2. Enter your SOP score:')
    LOR = st.number_input('2. Enter your LOR score:')
    Research = st.selectbox("Have you done any research",['Yes','No'])
    if Research == 'Yes':
        r = 1
    else:
        r = 0
    data = np.array([GRE, TOEFL, Rating, SOP, LOR, CGPA, r])
    if st.button('Predict Chance'):
        result  = predict(data)
        st.text(data)
        st.success("Congrats! Your Chance of admission is {} %".format(result[0] *100))
        if result[0] > 1:
            st.header("Your chance of admission is high.")
            st.balloons()
        else:
            st.warning('Man! you won\'t get it.')
    
    


if __name__ == "__main__":
    main()
