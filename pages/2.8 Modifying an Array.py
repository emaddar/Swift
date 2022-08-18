# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


def myStreamMarkDown(text):
    return st.markdown(text)

def myStreamCode(code, langauge = 'swift'):
    return st.code(code, language=langauge)

st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.8</h1>", unsafe_allow_html=True)

myStreamMarkDown("""
# Modifying an Array

An array's `append` method allows you to add a new item at the array's end.
""")

myStreamCode("""
var shoppingList = ["Bread", "Milk"]
shoppingList.append("Flour")
print(shoppingList)
// ["Bread", "Milk", "Flour"]
""")


myStreamMarkDown("""
Alternatively, add an array of one or more compatible items using the addition assignment operator **(+=)**:
""")

myStreamCode("""
shoppingList += ["Juise"]
shoppingList += ["Chocolate", "Cheese"]
print(shoppingList) 
//["Bread", "Milk", "Flour", "Juise", "Chocolate", "Cheese"]
""")


myStreamMarkDown("""
### Accessing an Array


Using subscript syntax, you can retrieve a value from the array, 
inserting the index of the value you want to retrieve within square brackets 
immediately after the name of the array:
""")
myStreamCode("""
var firstItem = shoppingList[0]
print(firstItem)
// Bread
""")

myStreamMarkDown("""
_Arrays in Swift are always zero-indexed, meaning that the first item's index is 0, rather than 1, as you might expect. Accessing or modifying a value for an index that is outside of an array's existing bounds triggers a runtime error. Check the validity of an index prior to using it by comparing it with the array's count property._
""")



myStreamMarkDown("""
### Modifying an Array
Use subscript syntax to change an existing value at a given index:
""")

myStreamCode("""
shoppingList[0] = "Two appeles"
print(shoppingList)
// ["Two appeles", "Milk", "Flour", "Juise", "Chocolate", "Cheese"]
""")


myStreamMarkDown("""
Subscript syntax also changes a range of values all at once. This will even work with a replacement set of values with a length that is different from the original range.
In the following example, the elements with index 1, 2, 3 are replaced with two new values.
""")

myStreamCode(""""
shoppingList[1...3] = ["Banans", "Oranges"]
print(shoppingList)
// ["Two appeles", "Banans", "Oranges", "Chocolate", "Cheese"]
""")


myStreamMarkDown("""
### Modifying an Array

An array's `insert` method will **insert** an item into the array at a specified index.
""")

myStreamCode("""
shoppingList.insert("Syrup", at : 0)
print(shoppingList)
// ["Syrup", "Two appeles", "Banans", "Oranges", "Chocolate", "Cheese"]
""")

myStreamMarkDown("""
"Syrup" is now the first item in the list.

Similarly, the `remove` method allows you to **remove** an item from the array. This method removes the item at the specified index, and also returns the removed item. Note that the returned value can be ignored if it is not needed.
""")

myStreamCode("""
let Syrup = shoppingList.remove(at : 0 )
print(Syrup)
// Syrup
""")

myStreamMarkDown(""" _When an item is removed from an array, Swift closes any gaps that have been created._ 

If you want to remove the final item from an array, use the `removeLast()` method rather than the removeAtIndex
 method to avoid the need to query the array's count property:
""")

myStreamCode("""
let appeles = shoppingList.removeLast()
// The last item has just been removed
""")

myStreamMarkDown("""
### Iterating Over an Array


The `for-in` loop allows you to iterate over the entire set of values in an array.
""")

myStreamCode("""
for i in shoppingList {
    print(i)
}
// Syrup
// Two appeles
// Banans
// Oranges
// Chocolate
""")


myStreamMarkDown("""
Alternatively, use the `enumerated()` method to iterate over an array when you need the integer 
index for each item in addition to its value. This returns a **_tuple_** for each item in the 
array that indicates that item's index and value.
 You can decompose the tuple into temporary constants or variables as part of the iteration:
""")


myStreamCode("""
for (index, value) in shoppingList.enumerated() {
    print("Item \(index+1) : \(value)")
}
// Item 1 : Two appeles
// Item 2 : Banans
// Item 3 : Oranges
// Item 4 : Chocolate
// Item 5 : Cheese
""")


myStreamMarkDown(""" _**Tuples** will be discussed in the upcoming lessons._ """)