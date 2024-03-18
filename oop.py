class Person:
    def __init__(self,name,age,gender): 
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello {self.name}, you are {self.age} years old and you are a {self.gender}")

prsn = Person("John",23,"male")
prsn.introduce()


        