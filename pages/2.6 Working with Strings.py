# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.6</h1>", unsafe_allow_html=True)

st.markdown("""
# Working with Strings


### Concatenation
String values can be added together (or concatenated) with the **addition operator (+)** to create a new String value:
""")

code = """
let string1 = "Hello" 
let string2 = " World" 
var welcome = string1 + string2 
// welcome now equals "Hello World"
"""

st.code(code, language='swift')

st.markdown("""
The addition assignment operator (+=) appends a String value to an existing String variable.
""")


code = """
var msg = "Hi" 
msg += " David" 
// msg is now "Hello David"
"""
st.code(code, language='swift')



















st.markdown("""
### String Interpolation
String interpolation includes the values of a mix of constants, variables, literals, and expressions inside a string literal to form a new String value. Prefix each item with a backslash, place the item in parentheses, and insert it into the string literal.
""")

code = """
let mult = 4 
let message = "\(mult) times 1.5 is \(Double(mult) * 1.5)" 
//message is "4 times 1.5 is 6.0"
"""

st.code(code, language='swift')

st.markdown("""
In the above example, the multiplier value is inserted into the string literal as \(mult). When the string interpolation is evaluated prior to creating the actual string, this placeholder is replaced with the actual value of mult.

Later in the string, the value of mult appears within a larger expression within the string literal: \(Double(mult) * 1.5). The expression calculates the value of Double(mult) * 1.5 and then inserts the result (6) into the string.
""")






st.markdown("""
### Counting Characters

To retrieve a **count** of the Character values in a string, use the `count` property of the string:literal to form a new String value. Prefix each item with a backslash, place the item in parentheses, and insert it into the string literal.
""")

code = """
let someString = "I am learning swift 4" 
print("somString has \(someString.count) charachters")
// somString has 21 charachters
"""

st.code(code, language='swift')


