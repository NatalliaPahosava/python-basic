if 5==5:
    print("yes")
    print("!!!!")

isHappy=True
if isHappy==True:
    print("User is happy")
if not isHappy:
    print("User is happy")

user_data=int(input("Input number"))
if user_data!=5:
    print("Number is not =5 ")
    if user_data>6:
        print("Number is bigger than 5")

isHappy=False
#### AND, OR  for using two conditions

if isHappy and user_data==6:
    print("User is happy")
elif user_data==5:
    print("Number is 5")
else:
    print("user is unhappy")

data=input()

number=5 if data=="Five" else 0

if data=="Five":
    number=5
else:
    number=0

print(number)
