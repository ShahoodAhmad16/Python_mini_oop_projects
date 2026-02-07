class TrafficSignal:
    def __init__(self, signal_id, duration):
        self.signal_id = signal_id
        self.current_color = 'RED'
        self.duration = duration

    def change(self):
        print(f'Signal changed to Green')

    def can_go(self, vehicle):
        print(f'{vehicle} can go')

    def status(self):
        print(f'Going')


class NormalSignal(TrafficSignal):
    def change(self):
        if self.current_color == 'RED':
            self.current_color = 'GREEN'
        elif self.current_color == 'GREEN':
            self.current_color = 'YELLOW'
        elif self.current_color == 'YELLOW':
            self.current_color = 'RED'

    def can_go(self, vehicle):
        if self.current_color == 'GREEN':
            return True
        else:
            return False


class PadestrianSignal(TrafficSignal):
    def change(self):
        if self.current_color == 'GREEN':
            self.current_color = 'YELLOW'
        elif self.current_color == 'YELLOW':
            self.current_color = 'RED'
        elif self.current_color == 'RED':
            self.current_color = 'GREEN'

    def can_go(self, vehicle):
        if self.current_color == 'RED':
            return True
        else:
            return False


class EmergencySignal(TrafficSignal):
    def change(self):
        self.current_color = 'GREEN'

    def can_go(self, vehicle):
        return True


class Vehicles:
    def __init__(self, plate_no, speed):
        self.plate_no = plate_no
        self.speed = speed

    def move(self):
        pass

    def get_priority(self):
        print(f'Priority: Low')


class Car(Vehicles):
    def move(self):
        print(f'{self.plate_no} car is moving with {self.speed} speed')

    def get_priority(self):
        print(f'{self.plate_no} Priority Low')


class Bus(Vehicles):
    def move(self):
        print(f'{self.plate_no} bus is moving with {self.speed} speed')

    def get_priority(self):
        print(f'{self.plate_no} Priority Low')


class Ambulance(Vehicles):
    def move(self):
        print(f'{self.plate_no} bus is moving with {self.speed} speed')

    def get_priority(self):
        print(f'{self.plate_no} Priority High')


car1 = Car('ABC123', 60)
bus1 = Bus('BUS321', 40)
ambulance1 = Ambulance('EMR789', 80)

signal1 = NormalSignal(1, 3)
signal2 = PadestrianSignal(2, 5)
signal3 = EmergencySignal(3, 6)

signal1.change()
if signal1.can_go(car1):
    print(f'{car1.plate_no} is moving')
else:
    print(f'{car1.plate_no} is waiting')
