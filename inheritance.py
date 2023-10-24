class Animal:
    def speaks(self):
        print(f"Animals Speaks")

class Cat(Animal):
    def meows(self):
        print(f"Cat Meows")
# initilaise an object
paka=Cat()
paka.meows()
paka.speaks()