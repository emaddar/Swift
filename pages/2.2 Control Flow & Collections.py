# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.2</h1>", unsafe_allow_html=True)

st.markdown("""
# The while Loop

A `while` loop performs a set of statements until a condition becomes false.
 These kinds of loops are best used when the number of iterations is not known before the first iteration begins.
while evaluates its condition at the start of each pass through the loop.
The while loop is demonstrated in the example below:
""")
code = """
while a < b {
    print(a)
    a += 1
}
"""

st.code(code, language='swift')

st.markdown("""
The code will execute until the a+=1 statement renders `a < b` as `false`.
""")





st.markdown("""
# Repeat-While

The `repeat-while` loop is the alternate while loop. 
It first makes a single pass through the loop block, 
then considers the loop's condition, and repeats the loop until the condition shows as false.
""")





code = """
repeat {
    x -= 1
} while  x > 0
"""

st.code(code, language='swift')


st.markdown("""
Swift's repeat-while loop is similar to a do-while loop in other languages.
""")





