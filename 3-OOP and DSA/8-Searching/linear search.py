list=[5,7,1,2,10,3]
searchnum=int(input("Please Enter Searching"))

def linearSearch():
    for i in range(len(list)):
        if list[i] == searchnum:
            return True

flag=linearSearch()
if flag==True:
    print("Your Target is found")
else:
    print("Your Target un founded")
