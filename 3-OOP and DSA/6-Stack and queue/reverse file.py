import Stack
def reverseFile(filename):
    original=open(filename,'r')
    s=Stack.stack()
    for line in original:
        s.push(line)
    original.close()

    output=open(filename,'w')
    while not s.is_empty():
        output.write(s.pop()+"\n")
    output.close()

reverseFile(r"C:\Users\Ayman Elkassas\Desktop\test.txt")


