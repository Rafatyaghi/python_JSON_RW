import json
import os

class Car:
    def __init__ (self, brand, productionYear, fuelType, colour, numberOfSeats):
        self.brand = brand
        self.productionYear = productionYear
        self.fuelType = fuelType
        self.colour = colour
        self.numberOfSeats = numberOfSeats

if __name__ == "__main__":
    brands=['Mercedes', 'BMW', 'Audi', 'Lamoborgini', 'Ferrari', 'Masarati', 'Porsche', 'Jaguar', 'Land Rover', 'Mercedes']
    productionYears = ['2020', '2019', '2020', '2016', '2019', '2010', '2019', '2019', '2020', '2016']
    fuelTypes = ['Diesel', 'Petrol', 'Diesel', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Diesel', 'Diesel', 'Petrol']
    colours = ['Dark Black', 'Dark Blue', 'Silver', 'Yellow', 'Red', 'Silver', 'Black', 'Black', 'Gold', 'Silver']
    numberOfSeats = [5, 5, 4, 2, 2, 2, 5, 5, 8, 5]

    #Another way to define the latter sets is using dictionary:
    car={
        'brand': ['Mercedes', 'BMW', 'Audi', 'Lamoborgini', 'Ferrari', 'Masarati', 'Porsche', 'Jaguar', 'Land Rover', 'Mercedes'],
        'productionYear': ['2020', '2019', '2020', '2016', '2019', '2010', '2019', '2019', '2020', '2016'],
        'fuelType': ['Diesel', 'Petrol', 'Diesel', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Diesel', 'Diesel', 'Petrol'],
        'colour': ['Dark Black', 'Dark Blue', 'Silver', 'Yellow', 'Red', 'Silver', 'Black', 'Black', 'Gold', 'Silver'],
        'numberOfSeats': [5, 5, 4, 2, 2, 2, 5, 5, 8, 5]
    }

    cars = list()
    cars_dict = list()
    for i in range(10):
        cars.append(Car(brands[i], productionYears[i], fuelTypes[i], colours[i], numberOfSeats[i]))
        cars_dict.append(cars[i].__dict__)
    
    with open("cars.json", "w+") as write_file:
        json.dump(cars_dict, write_file, indent=3)

    
    if os.path.isfile('cars.json'):
        with open('cars.json', 'r') as read_file:
            retrieved_cars = json.load(read_file)
    else:
        print("File does not exist")

    count = 1
    for i in retrieved_cars:
        print("car ", count,' : ',i)
        count+=1
