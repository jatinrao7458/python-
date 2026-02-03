# tuples
# the diff btw list and tupls is that tuple is immutable
marks=(22,44,34,554,554)
print(type(marks))
print(marks[1])

# to create a single element tuple we need to add commaa at last 
sin=(1,)
# if not comma means its is a int
print(sin)

# slicing
new =marks[1:3]
print(new)

# tuple method 
# index
# help us find the value of the specified index
nn= marks.index(44)
print(nn)

# count
# help us to find how many times a element is present
mm= marks.count(554)
print(mm)