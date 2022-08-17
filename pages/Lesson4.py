
# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("<h1 style='text-align: center; color: black;'>Lesson 4</h1>", unsafe_allow_html=True)

st.markdown("""
# Basic Operators

An **operator** is a special symbol or phrase used to check, change, or combine values.

Operators are unary, binary, or ternary:
- **Unary** Operator: Has a single target (-a). A unary prefix operator is placed before the target (!b).
- **Binary** Operator: Has two targets (4 + 5) and is infixed, appearing between the two targets.
- **Ternary** Operator: Has three targets. Like C, **_Swift has one ternary operator_**, the ternary conditional operator (a ? b : c).

The values targeted by operators are called operands. In the expression 1 + 2, the + symbol is a binary operator; its two operands are the values 1 and 2.


### Assignment Operator
The assignment operator (a = b) initializes or updates the value of `a` with the value of `b`

""")
code = """
let b = 7 
var a = 42 
a = b // a is now equal to 7
"""

st.code(code, language='swift')



st.markdown("""
### Arithmetic Operators

Swift supports the four standard arithmetic operators for all number types:

##### Addition (+)

""")
code = """
1+2 // equals 3
"""

st.code(code, language='swift')

































st.markdown("""
In practice, you will rarely need to add type annotations. Providing an initial value for a constant or a variable at the point at which it is defined, will almost always be sufficient for Swift to infer which type should be used:
""")
code = """
let pi = 3.14159 // Double
"""

st.code(code, language='swift')



st.markdown("""
Swift always chooses Double (as opposed to Float) when inferring the type for floating-point numbers.

Swift is a **type safe** language, meaning that it supports clarity when specifying value types for code. When part of your code expects a String, you can't pass it an Int by mistake.
""")

