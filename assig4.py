#ques1
list=[1,2,3,4,5]
list.reverse()
print(list)
#ques2
str1=input("enter the string\n")
upper=""
for letter in str1:
    if letter.isupper():
        upper=upper+letter+','
print(upper)        
#ques3
value=input('enter the input\n')
a=value.split(',')
b=[]
for i in b:
    b.append(int(i))
print(b)
#ques4
n=int(input("Enter number\n"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
#ques5
#shallow copy
import copy as c
list1=[1,2,[3,4],5]
list2=c.copy(list1)
list1[1]='hi'
print(list1)
print(list2)
#Deep copy
import copy as c
list1=[1,2,[3,4],5]
list2=c.deepcopy(list1)
list1[2][0]='hi'
print(list1)
print(list2)
