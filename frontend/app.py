import streamlit as st

st.title("Hello, Traveller!")
st.write("Welcome to the world of TravelAgent. Helps to give you the best travel deals.")

name = st.text_input("What's your name?")
budget = st.number_input("What's your travel budget?", min_value=0,step=100)
days = st.slider("How many days do you want to travel?", min_value=1, max_value=30)

if st.button("Find me a deal!"):
    st.write(f"Great, {name}! Let me find you the best travel deals for a {days}-day trip with a budget of ${budget}.")
    # Here you would typically call your backend API to get travel deals based on the user's input
    # For demonstration purposes, we'll just show a placeholder message
    st.write("Fetching travel deals... (This is where the magic happens!)")