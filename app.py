import streamlit as st

# Title of the app with an emoji
st.title("Simple Calculator 🧮")

# Input fields for two numbers
num1 = st.number_input("Enter the first number 🔢", value=0.0)
num2 = st.number_input("Enter the second number 🔢", value=0.0)

# Dropdown menu to select the operation with emojis
operation = st.selectbox(
    "Choose an operation ➗", 
    ("Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗")
)

# Perform the selected operation
if operation == "Addition ➕":
    result = num1 + num2
elif operation == "Subtraction ➖":
    result = num1 - num2
elif operation == "Multiplication ✖️":
    result = num1 * num2
elif operation == "Division ➗":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero! ❌"

# Display the result with emojis
st.write(f"The result of {operation} is: {result} 🎉")

