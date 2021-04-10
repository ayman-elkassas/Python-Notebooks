def removeSpesialChar(st=""):
    for chars in st:
        if type(chars) is str:
            st.strip(chars)
    return st
print(removeSpesialChar("let's go , frank"))