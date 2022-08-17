# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.3</h1>", unsafe_allow_html=True)

st.markdown("""
# The for-in Loop

Use the `for-in loop` to iterate over a sequence, 
such as ranges of numbers, items in an array, or characters in a string.
The following example prints the first few entries in the five-times-table:
""")
code = """
for index in 1...5 {
    print("\(index) times 5 is \(index * 5) ")
}
//1 times 5 is 5 
//2 times 5 is 10 
//3 times 5 is 15 
//4 times 5 is 20 
//5 times 5 is 25
"""

st.code(code, language='swift')

st.markdown("""
The index variable is set at the first value in the range (1). 
The statements within the for loop are then executed in sequence, through the final item in the range (5).
""")
