import Stack
S=Stack.stack()
s=[]
for i in range(3):
    S.push(i+1)
# print(len(S))
for j in range(3):
    s.append(S.pop())
print(s)

