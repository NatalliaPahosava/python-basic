# comments
#just hashgtag Print() function

print('sasha')
print("Result: ",5)
# SEP 
print("Result:",5, sep="")
print('second line')
#End-new line
print("Result:",5, sep="",end="\n")
print('second line')
print("Result:",5, sep="",end="!\n")
print('second line')
print('second \' line')

#math
print('Result:',5**5)
#modulus
print('Result:',7//5)
# min()
print("result:", min(3,4,5,6,7))
#max()
print("result:", max(3,4,5,6,7))
#pow(a,b)
print("result:",pow(5,3))
#round(a/b)
print("result:",round(5 / 3))

#input()

input("Enter your age:")

#########################
########Variable#########

number = 5
print(number)
number=7
print(number)

del number
number=5 #integer
digit = -5.334444     # float
word="Result:"  #string
boolean=False   #boolean

print(word,digit,boolean)
#str()
print(word,str(digit),boolean)

str_num="5"   #string
#int()
print(number + int(str_num))
#never do defferent data type
#print(word+number+boolean)