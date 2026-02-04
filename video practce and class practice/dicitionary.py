# dicitionaries are used to store valus in key:value pair
# all typess of value are permitted in dicitionary for value
# but key cannot use dicitionary and list bcz they are mutable 
# dictionary are unordered as they have no index
info = {
    "name":"jatin",
    "age ": 19
}
print(info)
# to acces its value we use key of the dict
print(info["age "])
# updating value
info["age "]= 20
print(info)
# adding new pair
info["Uni"]="SGT"
print(info)

# nested dictionary
student= {
    "name":"Jatin",
    "marks":{
        "english":23,
        "maths":45,
        "Science":88
    }
}
print(student)
print(student["marks"])
print(student["marks"]["maths"])


# dictionary methods
# .keys - to gett all keys printed in a list format
print(info.keys())

# length
# tells number of key value pair
print(len(info))


# values
# returns collection of all values
print(info.values())

# items
# returns all key value pair as tuples
print(info.items())

# get 
# to get value of specified key
print(info.get("name"))
print(info["name"])
# the above values returns the same value 
# the diff btw the two is that when ever we pass a key which is not defined then the .get method will not give an error whereas the square bracket method gives error 

# update
# to pass nw key value pairs
info.update({
    "city":"delhi"
})