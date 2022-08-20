# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


def myStreamMarkDown(text):
    return st.markdown(text)

def myStreamCode(code, langauge = 'swift'):
    return st.code(code, language=langauge)

st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.10</h1>", unsafe_allow_html=True)

myStreamMarkDown("""
# Set Operations
Swift allows you to efficiently perform fundamental **set operations**,
 such as combining sets, determining which values two sets have in common,
  or determining whether two sets contain all, some, or none of the same values.

### Fundamental Set Operations

The illustration below depicts sets **a** and **b**, and shows the results of various set operations, 
as represented by the shaded regions:
""")

st.image(
            "https://api.sololearn.com/DownloadFile?id=3381",
            width=500, # Manually Adjust the width of the image as per requirement
        )



myStreamMarkDown("""
- The `intersection` method creates a new set, with only the values common to both sets.
- The `symmetricDifference` method creates a new set with values in either set, but not both.
- The `union` method creates a new set with all of the values in both sets.
- The `subtracting` method creates a new set with values not in the specified set.

For example, to combine the two sets:
""")



myStreamCode("""
let oddDigits : Set = [1, 3, 5, 7, 9]
let evenDigits : Set = [0, 2, 4, 6, 8]
print(oddDigits.union(evenDigits).sorted())
// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
""")


myStreamMarkDown("""
### Set Membership and Equality


The illustration below depicts three sets: `a`, `b`, and `c`. 
The overlapping regions represent the elements that are shared among sets.

- Set **a** is a `superset` of set **b**, because **a** contains all elements in **b**.
- Conversely, set **b** is a `subset` of set **a**, because all elements in **b** are also contained by **a**.
- Sets **b** and **c** are `disjointed` with one another, because they share no elements in common.
""")


st.image(
            "https://api.sololearn.com/DownloadFile?id=983",
            width=500, # Manually Adjust the width of the image as per requirement
        )

myStreamMarkDown("""
- **is equal** operator (`==`): Determines whether two sets contain all of the same values.
- `isSubset(of: )` method: Determines whether all of the values of a set are contained in the specified set.
- `isSuperset(of: )` method: Determines whether a set contains all of the values in a specified set.
- `isStrictSubset(of: )` or `isStrictSuperset(of: )` method: Determines whether a set is a subset or superset of, but not equal to, a specified set.
- `isDisjoint(with: )` method: determines whether two sets have any values in common.
""")

myStreamCode("""
print(oddDigits.isStrictSuperset(of: evenDigits)) 
// false
""")