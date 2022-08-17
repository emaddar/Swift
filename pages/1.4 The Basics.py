
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
1 + 2 // equals 3
"""

st.code(code, language='swift')



st.markdown("""
##### Subtraction (-)
""")
code = """
6 - 2 // equals 4
"""

st.code(code, language='swift')






st.markdown("""
##### Multiplication (*)
""")
code = """
4 - 3 // equals 12
"""

st.code(code, language='swift')


st.markdown("""
##### Division (/)
""")
code = """
10.0 - 2.5 // equals 4
"""

st.code(code, language='swift')



st.markdown("""
##### The addition operator is also supported for **String concatenation**:
""")
code = """
"Hello, "+ "world" // equals "Hello, world"
"""

st.code(code, language='swift')




st.markdown(r"""
### Remainder Operator

The remainder operator `(a % b)` calculates the number of multiples of `b` that fit within `a`, and returns the value that is left over, or the **remainder**
""")

code = """
9 % 4 // equals 1
"""

st.code(code, language='swift')

st.markdown(r"""
In other languages, the remainder operator (%) is called a modulo operator. In Swift, however, its behavior for negative numbers means that it is, strictly speaking, a **remainder**, rather than a modulo operation.
""")





st.markdown(r"""
### Compound Operators

Like C, Swift provides compound operators that combine assignment (=) with another operation.
""")

code = """
var a = 1
a += 2 // a equals to 3
"""

st.code(code, language='swift')

st.markdown(r"""
The expression a += 2 is shorthand for a = a + 2. The addition and the assignment are combined into one operator that performs both tasks at the same time.
Similarly, there are shorthand operators for other arithmetic operations.
""")
