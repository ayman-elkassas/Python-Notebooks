import os
def sizeofpath(path):
    total = 0
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath=os.path.join(path,filename)
            total+=sizeofpath(childpath)
    else:
        total=os.path.getsize(path)

    return total
print(sizeofpath(r"C:\Users\Ayman Elkassas\Desktop\wireshark.txt")," ")


