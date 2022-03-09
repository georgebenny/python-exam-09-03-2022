str=input("Enter a string:")
print("The string before replacing",str)
a=str[0]
str1=str.replace(a,"$")
x=a+str1[1:]
print("The string after replace",x)

