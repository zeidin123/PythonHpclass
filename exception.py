# name="zeinab"
#
# for i in name:
#     if i != 0:
#     prin(i))

fruits = ["Mangoes", "Apples", "Oranges"]
try:
    for i in range(6):
        print(f"The index and element from the list is {i, fruits[i]}")
except:
    print("index out of range")
nambar=[3,4,5,7]
if len(nambar)>3:
    raise Exception(f"Length of the given list must be less or equal to 3 but its {len(nambar)}")
