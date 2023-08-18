import streamlit as st
from functions import predict, load_data


st.set_page_config(
    page_title = 'Early Diabetes Prediction',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

df, X, y = load_data()

def app(df, X, y):
    st.title("Prediction Page")

    st.subheader("Select Values:")

    glucose = st.slider("Glucose", int(df["Glucose"].min()), int(df["Glucose"].max()))
    bp = st.slider("Blood_Pressure", int(df["Blood_Pressure"].min()), int(df["Blood_Pressure"].max()))
    insulin = st.slider("Insulin", int(df["Insulin"].min()), int(df["Insulin"].max()))
    bmi = st.slider("BMI", float(df["BMI"].min()), float(df["BMI"].max()))
    pedigree = st.slider("Pedigree_Function", float(df["Pedigree_Function"].min()), float(df["Pedigree_Function"].max()))
    age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
    features = [glucose, bp, insulin, bmi, pedigree, age]

    if st.button("Predict"):
        prediction, score = predict(X, y, features)
        st.success("Predicted Sucessfully")
        if (prediction == 1):
            st.info("The person either has diabetes or prone to get diabetes")
        else:
            st.info("The person is free from diabetes")

        st.write("The accuracy score of this model is", score)

app(df, X, y)