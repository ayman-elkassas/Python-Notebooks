def vowels(st):
    count=0
    listchar=[]
    for char in st:
        if char in ('a','e','i','o','u','A','E','I','O','U') and char not in listchar:
            count+=1
        listchar.append(char)

    return count

print(vowels("ae for vowlous"))