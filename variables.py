cars=100
space_in_a_car = 4.0
drivers = 30.0
passengers = 90.0
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_a_car
average_passenger_per_car= passengers/cars_driven
print("There are", cars, "cars available.")
print("There are only", drivers , "drivers available")
print("There will be", cars_not_driven, "cars empty")

#it can be used in this way