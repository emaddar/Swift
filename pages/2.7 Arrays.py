# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.7</h1>", unsafe_allow_html=True)

st.markdown("""
# Arrays

An array is an ordered list of values of the same type, 
in which the same value can appear multiple times at different positions. 
In Swift, the array type can be written in full as **Array<T>**, in which **T** represents 
which value type the array is allowed to store. 
The array type can also be expressed in shorthand form, as **[T]**.
Although the two forms are identical in function, the shorthand will appear throughout this tutorial in reference to an array type.

### Creating an Empty Array


Create an empty array of a certain type using initializer syntax.
""")

code = """
var somInts = [Int]()
"""
st.code(code, language='swift')


st.markdown("""
Note that the type of the _someInts_ variable is inferred to be **[Int]**, from the type of the initializer.

### Array with a Default Value


Swift's Array type also provides an initializer for creating an array of a certain 
size with all of its values set to the same default value. 
You pass this initializer the number of items to be added to the new array
 (called **count**) and a default value of the appropriate type (called **repeating**):
""")

code = """
var fourDoubles = [Double](repeating : 0.0 , count : 4)
print(fourDoubles)
// [0.0, 0.0, 0.0, 0.0]
"""

st.code(code, language='swift')






st.markdown("""
### Array Literal

Using an array literal is another way to initialize an array. The array literal is shorthand for one or more values written as an array collection, and is written as a list of values, separated by commas, with square brackets at beginning and end.

The example below creates an array called shoppingList, for storing String values:
""")

code = """
var shoppingList = [String]("Bread", "Milk")
"""
st.code(code, language='swift')

st.markdown("""
This particular array can store only String values, as it has String specified as its value type.

Because of Swift's type inference, you **don't have to** write out the array type. Be sure to initialize with an array literal containing values of that same type. The initialization of shoppingList could have been written in a shorter form:
""")





code = """
var shoppingList = ["Bread", "Milk"]
"""
st.code(code, language='swift')

st.markdown("""
All values in the array literal are of the same type, enabling Swift to infer that [String] is the correct type for the shoppingList variable.

_Combining two existing arrays with compatible types using the addition operator (+) allows you to create a new array. Swift infers the new array's type based on the type of the two combined arrays._
""")






















st.markdown("""
### Accessing and Modifying an Array

Access and modify an array through its methods and properties or by using subscript syntax.

An array's read-only `count` property provides the number of items in an array.
""")

code = """
print("The shoping list contains \(shoppingLis.count) itmes ")
"""
st.code(code, language='swift')

st.markdown("""
Use the Boolean isEmpty property as a shortcut when you want to know whether the count property is equal to 0.
""")

code = """
if shoppingList.isEmpty {
    print("List is Empty")
} else {
    print("List is not Empty")
}
// List is not Empty
"""

st.code(code, language='swift')