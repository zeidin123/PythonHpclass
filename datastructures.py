# list
mylist = ["Erick", "Joan", "Mercy", "Daniel", "Gloria", "Brian"]
mylist2 = [89, 12, 17, 34, -1, -45]
mylist2.sort()
mylist.sort()

print(mylist)
print(f"My name is {mylist[0]}")
print(f"My name is " + mylist[0])
print(f"My name is " + mylist[1])
print(f"My name is " + mylist[2])
print(f"My name is " + mylist[3])
print(f"My name is " + mylist[4])
print(f"My name is " + mylist[5])
print(f"My sorted list {mylist2}")

# tuple same as list but tuple is immutable(cant change its value)
my_tuple = ("Palestine", "Kenya", "Uganda", ["Egypt", "Lebanon"], "Morocco", "Egypt", "Yemen", "Syria")
# my_tuple[2]  = "Dubai" error
print(my_tuple)
print(f"My country is {my_tuple[0]}")

# set unordered
fruits = {"Oranges", "Pinneapples", "Bananas", "Apples"}
print(fruits)

# dictionaries
employees = {"Name": "Zeinab", "Age": 30, "Gender": "Female", "salary": 1000000}
print("Employees Name :%s" % employees["Name"])
print("Employees Name :%d" % employees["Age"])