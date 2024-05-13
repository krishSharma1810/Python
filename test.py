# a calculator
# num1 = int (input("num1"))
# ans=num1
# oper=input("operator")

# while oper != '=':
#     if oper=='+':
#         num2 = int (input("num2"))
#         ans=ans+num2
#         oper=input("operator")
#     elif oper=='-':
#         num2 = int (input("num2"))
#         ans=ans-num2
#         oper=input("operator")
#     elif oper=='*':
#         num2 = int (input("num2"))
#         ans=ans*num2
#         oper=input("operator")
#     elif oper=='/':
#         num2 = int (input("num2"))
#         ans=ans/num2
#         oper=input("operator")
#     else:
#         print('enter a valid operator')
# print(ans)





# tupples

# creating tupple
x=()
print(x)


# empty tupple
tuplex=tuple()
print(tuplex)


# create a tupple with different data types
tuplx=('tupple',False,3.2,3)
print(tuplx)


# unpack a tupple
tup=4,8,3
print(tup)
n1,n2,n3=tup
print(n1+n2+n3)
# n1,n2,n3,n4=tup


# to find index and item in tupple
tu=tuple("index tuple")
print(tu)
index=tu.index('p')
print(index)
index=tu.index('p',5)
print(index)
index=tu.index('e',3,6)
print(index)
# index=tu.index('y')
# print(index)


# add item in tuple
tup=(4,6,2,8,3,1)
print(tup)
tup=tup+(9,)
print(tup)


# add item at specific index
tup=tup[:5]+(15,20,25)+tup[:5]
print(tup)
listx=list(tup)
listx.append(30)
tup=tuple(listx)
print (tup)



# tupple to string
tuplexx=("n","a","m","e")
print(tuplexx)
str="".join(tuplexx)
print(str)