def add(*args):
    sum_total = 0
    for n in args:
        sum_total += n
    return sum_total


print(add(1,2,3,4,5,6,7,8,9,10))


def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))


calculate(add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.model = kw.get("color")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.color)