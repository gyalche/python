str1 = "this is string one"
len1 = len(str1)
print(len1)
print(str1[0])

#slicing
print(str1[0:4])

#slicing negative index (-)

print(str1.endswith("one"))
print(str1.capitalize())
print(str1.replace("i", "b"))
print(str1.split(" "))
print(str1.find("string"))

name = input("enter your name")
print("length of name is ", len(name))

#conditional statement;

num = 5
if num > 0:
    print("number is positive")
elif num == 0:
    print("number is zero")
else:
    print("number is negative")