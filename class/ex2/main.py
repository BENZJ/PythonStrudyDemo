from car import Car
from electric_car import ElectricCar
my_new_car = Car('audi','a4',2016)
print "---This is a car class output----"
print my_new_car.get_descriptive_name()
my_new_electric_car  = ElectricCar('tesla','model s', 2016, 70)
print "\n\n---This is a ElectricCar class output---"
print my_new_electric_car.get_descriptive_name()
my_new_electric_car.describe_bettery()
