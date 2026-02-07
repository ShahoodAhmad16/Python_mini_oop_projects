class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f'Vehicle is starting')

    def stop(self):
        print(f'Vehile is stoping')

    def info(self):
        print(f'''Brand: {self.brand}
Model: {self.model}
Year: {self.year}
''')


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print(f'{self.brand} {self.model} is starting')

    def stop(self):
        print(f'{self.brand} {self.model} is stoping')

    def info(self):
        print(f'''Brand: {self.brand}
Model: {self.model}
Year: {self.year}
Number of doors: {self.number_of_doors}
''')


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def start(self):
        print(f'{self.brand} {self.model} is starting')

    def stop(self):
        print(f'{self.brand} {self.model} is stoping')

    def info(self):
        print(f'''Brand: {self.brand}
Model: {self.model}
Year: {self.year}
Has Sidecar: {self.has_sidecar}
''')


class Truck(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def is_old(self):
        if self.year > 0:
            if self.year > 10:
                print(f'OLD/NEW: {self.model} {self.brand} is Old')
            else:
                print(f'OLD/NEW: {self.model} {self.brand} is New')

        else:
            print(f'Negative number not allowrd')

    def start(self):
        print(f'{self.brand} {self.model} is starting')

    def stop(self):
        print(f'{self.brand} {self.model} is stoping')

    def info(self):
        print(f'''Brand: {self.brand}
Model: {self.model}
Year: {self.year}
''')
        self.is_old()


vehicles: list[Vehicle] = [
    Car('Audi', 'S8', 2025, 4),
    Motorcycle('Yamaha', 'Suzuki', 2025, True),
    Truck('Merserk', 'New', 15),
]

vehicle_type = int(input(f'''1: Car
2: Motorcycle
3: Truck
'''))
if vehicle_type == 1:
    brand = input('brand:  ')
    model = input('model:  ')
    year = input('year: ')
    number_of_doors = input('Number of doors: ')
    vehicles.append(Car(brand, model, year, number_of_doors))
elif vehicle_type == 2:
    brand = input('brand:  ')
    model = input('model:  ')
    year = input('year: ')
    sidecar = input('sidecar: ')
    vehicles.append(Motorcycle(brand, model, year, sidecar))
elif vehicle_type == 3:
    brand = input('brand:  ')
    model = input('model:  ')
    year = int(input('year: '))
    vehicles.append(Truck(brand, model, year))
else:
    print('Option doesnt exits')

car_count = 0
motorcycle_count = 0
truck_count = 0
for vehicle in vehicles:
    print('*'*20)
    vehicle.info()
    print(f'Type: {type(vehicle).__name__}')
    vehicle.start()
    vehicle.stop()
    print('*'*20)
    if type(vehicle) is Car:
        car_count += 1
    if type(vehicle) is Motorcycle:
        motorcycle_count += 1
    if type(vehicle) is Truck:
        truck_count += 1
print(f'Car: {car_count}')
print(f'Motor Cycle: {motorcycle_count}')
print(f'Truck: {truck_count}')
