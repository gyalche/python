#List and tuples
# A list is a mutable, ordered collection of items. Lists are defined using square brackets [].
marks = [85, 90, 78, 92, 88]
print("Original list of marks:", type(marks))
print(marks[0])
print(len(marks))

student  = ["Alice", 20, "A"]

print(student[0:3])
student[0] = "dawa"
print(marks.sort())
print(marks)

#sort in descending order;
marks.sort(reverse=True)
print(marks)

#reverse list;
marks.reverse()
print(marks)

#insert element in list;
marks.insert(2, 00)
print(marks)

#remove from list;
marks.remove(00)
print(marks)
print(marks.pop(1))
#strings are immutable in python, list are mutable in pythong;


#Tuples;
# A tuple is an immutable, ordered collection of items. Tuples are defined using parentheses ().

tup = (1,2,3,4,5)
print(type(tup))

#palindrome;
list1 = [1,2,3,2,1]
list2 = [1,2,3,4,5]

copy_list1 = list1.copy()
copy_list1.reverse()
if list1 == copy_list1:
    print("palindrome")
else:
    print("not palindrome")

#total no of occurrence of an element in a list;
grade=("A", "B", "C", "A", "B", "A")
print(grade.count("A"))

