# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.4</h1>", unsafe_allow_html=True)

st.markdown("""
# Control Transfer

Control transfer statements alter the code execution by transferring control from one piece of code to another. 
Swift's four control transfer statements are continue, break, fallthrough, and return 
(which will be discussed in the upcoming lessons).

### Continue

The continue statement stops the loop, then restarts it at the beginning of its next cycle.
The example below shows how to use the continue statement to skip over even numbers.
""")

code = """
for num in 1...10 { 
    if num%2 == 0 { 
        continue 
    } 
    print(num)
}
"""

st.code(code, language='swift')

st.markdown("""
A for loop with a condition and an incrementer still evaluates the incrementer after the continue statement is initiated. The loop itself continues to work as usual; only the code within the loop's body is skipped.
""")












st.markdown("""
### Break

Use the **break** statement to immediately end the execution of an entire control flow statement. 
Also, the break statement is used within a switch statement or a loop statement to terminate 
its execution sooner than would otherwise be the case.


##### Break in a Loop Statement

When a break statement is used within a loop statement, the loop's execution immediately stops. 
Control transfers to the first line of code following the loop's closing brace (}). The current iteration's remaining code is skipped, and no further iterations of the loop are initiated.
For example, you can have a loop that breaks out when the value of **a** becomes less than that of **b**:


""")

code = """
var b = 7
var a = 10
while a > 0 {
     if (a<b) {
         break
    } 
    print(a) 
    a -= 1
}
//10
//9
//8
//7
"""

st.code(code, language='swift')

st.markdown("""
##### Break in a Switch Statement

A **break** causes a switch statement to end its execution immediately, 
and transfers control to the first line of code that follows the switch statement's closing brace (}).
""")

code = """
var a = 5 
var letter = "X"

switch a {
    case 1:
     letter = "A" 
    case 2 : 
     letter = "B" 
    default : 
     break 
}
"""

st.code(code, language='swift')

st.markdown("""
This example breaks out of the switch statement as soon as the default case is matched.

**_Always use a break statement to ignore a switch case._**
""")





























st.markdown("""
##### Fallthrough

In Swift, switch statements do not fall through the bottom of each case into the next. 
Instead, the entire switch statement completes its execution when the first matching case is completed.
By contrast, C requires insertion of an explicit break statement at the end of every switch case 
to prevent fallthrough. By eliminating default fallthrough, Swift allows for more concise and 
predictable switch statements in comparison with C, and thus avoids inadvertently executing multiple switch cases.
""")

code = """
let myInt = 5 
var desc = "The number \(myInt) is"
switch myInt {
    case 2,3,5,7,11,13,17,19 : 
        desc += " a prime number, and also" 
        fallthrough 
    default : 
        desc += " an integer"
} 
print(desc)
// The number 5 is a prime number, and also an integer
"""

st.code(code, language='swift')

st.markdown("""
If myInt's value is one of the prime numbers in the list, text noting that the number is prime is appended to the end of the description. The fallthrough keyword then causes it to "fall into" the default case.

_The fallthrough keyword does not check case conditions in the switch case into which execution falls. As with C’s standard switch statement behavior, the fallthrough keyword moves code execution directly to the statements inside the next (or default) case block._
""")