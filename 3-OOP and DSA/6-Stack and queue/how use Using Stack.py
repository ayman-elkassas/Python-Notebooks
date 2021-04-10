# Stack is (LIFO) last in first out
# Ex:plates (الاطباق)

# basic functions in stack :
# 1- S.push(e) ---------> Add e object as a top element of stack
# 2- S.pop() -----------> Return top object with remove it from elements of stack
# 3- S.top() -----------> Return top object without remove it from elements of stack
# 4- S.is_empty() ------> if stack is empty
# 5- len(S) ------------> return number of elements of stack

import Stack
S=Stack.stack()
S.push(5)
S.pop()
print(S.is_empty())