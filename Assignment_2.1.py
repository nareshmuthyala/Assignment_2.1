inputStr = input("Please enter the sequence of numbers seperated by comma :")
list1 = list()
for char in inputStr:
    if(char != ','):
        list1.append(int(char))
print(list1)