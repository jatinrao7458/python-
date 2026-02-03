# list 
from os import remove


marks =[23,45,67,89,12]
# data can be of diff types
print(marks)
print(type(marks))
print(len(marks))
print(marks[3])
marks_and_student =["jatin",23,"Jay",45,67,89,12]
print(marks_and_student)
# strings are immutable in py
# lists are mutable in py

# slicing
# ending index is never considered in slicing
new= marks[1:3]
print(new)
# negative index is also possible here
new_new= marks[-4:-2]
print(new_new)

# list methods

# append
# add element to the last of the list
append = marks.append(4)
print(append)
print(marks)

# sort 
# sorts in ascending order
sort = marks.sort()
print(sort)
print(marks)
# sorts in decending methos
sort_dece = marks.sort(reverse=True)
print(marks)
# sorting can be done on letters also
fruits=['banana','apple','watermelon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# reverse
marks.reverse()
print(marks)

# insert
# similiar to append but the diff is that insert can add at any index whereas append only adds at the last
marks.insert(2,33)
# this line of code means that 33 is added at the index number 2
print(marks)

# remove
# removes the first occurence of the lis 
# like if i want to remove 1 form the list it will remove first 1 number from the list
marks.remove(33)
print(marks)

# pop
# remove element from the specific index specified
marks.pop(2)
print(marks)



