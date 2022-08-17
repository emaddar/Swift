# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("<h1 style='text-align: center; color: black;'>Lesson 6</h1>", unsafe_allow_html=True)

st.markdown("""
# Optionals

Optionals are used in situations in which a value **may be absent**.

An optional says:
- There is a value, and it equals x
or
- There isn't a value at all
""")
code = """
var myCode : Int? = 404
"""

st.code(code, language='swift')

st.markdown("""
An optional Int is written as **Int?**, not Int. 
The question mark indicates that the value contained within is **optional**,
 meaning that it might contain some Int value, or it might contain no value at all.

 It can't contain anything else, such as a Bool value or a String value. It's either an **Int**, or it's nothing at all.
""")



















st.markdown("""
# nil

You set an optional variable to a valueless state by assigning it the special value **nil**:
""")
code = """
var myCode : Int? = 404
myCode = nil // myCode now contains no value

"""

st.code(code, language='swift')

st.markdown("""
An optional variable with no default value is automatically set to nil for you:
""")

code = """
var someMsg : String?
// someMsg is automatically set to nil

"""

st.code(code, language='swift')


st.markdown("""
_**nil** cannot be used with non-optional constants and variables. If your code contains a constant or variable that needs to work with the absence of a value under certain conditions, always declare it as an optional value of the appropriate type_.
""")