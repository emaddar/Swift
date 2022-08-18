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

st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.9</h1>", unsafe_allow_html=True)

myStreamMarkDown("""
# Sets
A set stores distinct values of the same type in a collection with no defined ordering.
 **Sets are used as an alternative to arrays when item order is not a concern or when you 
 need to ensure that an item appears only once.**
For a Swift set, write the type as **Set<T>** where **T** is the type that the set is allowed to store. 
Unlike arrays, there is no equivalent shorthand for sets.
You can create an empty set of a certain type using initializer syntax:
""")

myStreamCode(""" let letter = Set<Character>() """)

myStreamMarkDown("""
An array literal will also work as shorthand when initializing a set with one or more values as a set collection.
""")


myStreamCode("""
var names : Set<String> = ["David", "Susan", "Robert"]
print(names)
// ["Susan", "Robert", "David"]
""")


myStreamMarkDown("""
When initializing the type of set with an array literal that contains values of the same type, it is not necessary to write the type of set. The initialization could have been written in a shorter form:
""")


myStreamCode(""" var names : Set = ["David", "Susan", "Robert"] """)

myStreamMarkDown("""
_Because all values in the array literal are of the same type, Swift infers that ***Set<String>*** is the correct type to use for the names variable._
""")

myStreamMarkDown("""
### Accessing and Modifying a Set


The `count` and `isEmpty` properties work the same way with a set as they do with an array.
Calling the set's `insert` method adds a new item to a set.
""")

myStreamCode("""
names.insert("Paul")
print(names)
// ["Susan", "Robert", "David"]
""")


myStreamMarkDown("""
You can remove an item from a set by calling the set's `remove` method. The item is 
removed if it's a member of the set, and the removed value is returned. 
It returns nil if the item is not contained in the set. Alternatively, use the set's `removeAll()` method to remove all of the items in a set.

The `contains` method tells you whether or not a particular item is present in the set.
""")

myStreamCode("""
if names.contains("James"){
    print("James is here")
} else {
    print("James is not here")
} 
// James is not here
""")

myStreamMarkDown("""
### Iterating Over a Set

You can iterate over the values in a set with a `for-in` loop.
""")

myStreamCode("""
for i in names {
    print(i)
}
// Susan
// Paul
// David
// Robert
""")

myStreamMarkDown("""
Since Swift's Set type does not provide defined ordering, use the `sorted()` method to iterate over the values of a set in a specific order.
""")

myStreamCode("""
for i in names.sorted() {
    print(i)
}
// David
// Paul
// Robert
// Susan
""")