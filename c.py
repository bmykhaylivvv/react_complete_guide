class Person():
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname



class Child(Person):
  def __init__(self, name, surname, age):
    super().__init__(name, surname)
    self.age = age


person1 = Person("Mark", "Zuck")
child1 = Child("Jack", "London", 18)
print(child1.age)