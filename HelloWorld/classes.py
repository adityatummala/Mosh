class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Classes are used to create new types. In here, we have created a type called point and created
# functions/methods that will work with this point.
# now we will create an object to create an instance of that class

point_test = Point()
point_test.draw()
point_test.x = 10
print(point_test.x)

# Objects can also have attributes/variables that belong to this object
# Constructors

point_test_c = Point2(40,50)
print(point_test_c.x)
print(point_test_c.y)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")

person_test = Person("Aditya")
person_test.talk()
print(person_test.name)

