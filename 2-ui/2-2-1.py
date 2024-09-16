import streamlit as st

def calculate_dimensions(length, width):
    perimeter = length*2 + width*2
    area = length * width
    st.write(f"Perimeter is {perimeter}!")
    st.write(f"Area is {area}!")
    return

st.title("Calculating Area and Perimeter.")
length = st.number_input("Length: ")
width = st.number_input("Width: ")
calculate_dimensions(length, width)


