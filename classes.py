# Testing assigning an object to a variable
class Facade:
    pass

facade_1 = Facade()

facade_1_type = type(facade_1)

print(facade_1_type)

# Testing accessing attributes of an object
class Musician:
    title = "Rockstar"

drummer = Musician()
print(drummer.title)


# Testing calling a method that uses an attribute to generate an output
class Dog():
    dog_time_dilation = 7

    def time_explanation(self):
        print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()

print(type(pipi_pitbull))


# Testing using an object method to calculate an output
class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)


# Testing the __init__ functionality of classes
class Shouter:
    def __init__(self):
        print("HELLO?!")

shout1 = Shouter()

shout2 = Shouter()


# Testing initiating an object with a parameter
class Shouter:
    def __init__(self, phrase):
        # make sure phrase is a string
        if type(phrase) == str:
            # then shout it out
            print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"


# Another test class
class Circle:
    pi = 3.14
    def area(self, radius):
        return self.pi * radius ** 2

circle = Circle()

pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(11460/2)


# Another test class
class Circle:
    pi = 3.14
    def __init__(self, diameter):
        print('New circle with diameter: {}'.format(diameter))

teaching_table = Circle(36)


# Testing empty object editting
class FakeDict:
    pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)


# Another test
class Store:
    pass

store = Store()

store.alternative_rocks = "Alternative Rocks"
store.isabelles_ices = "Isabelle’s Ices"