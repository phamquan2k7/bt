import random
# 1. Elevator class
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()
# 2 + 3. Building class
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, index, target_floor):
        if 0 <= index < len(self.elevators):
            print(f"\nRunning elevator {index}")
            self.elevators[index].go_to_floor(target_floor)
        else:
            print("Invalid elevator index")

    def fire_alarm(self):
        print("\nFIRE ALARM! All elevators go down...")
        for e in self.elevators:
            e.go_to_floor(self.bottom)
# 4. Car + Race
class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print("\n--- Race Status ---")
        for car in self.cars:
            print(f"{car.reg}: speed={car.speed} km/h, distance={car.distance} km")

    def race_finished(self):
        return any(car.distance >= self.distance for car in self.cars)
# Test Elevator
print("=== Elevator Test ===")
e = Elevator(1, 10)
e.go_to_floor(5)
e.go_to_floor(1)

# Test Building
print("\n=== Building Test ===")
b = Building(1, 10, 3)
b.run_elevator(0, 7)
b.run_elevator(1, 3)
b.fire_alarm()

# Test Race
print("\n=== Race Simulation ===")
cars = []
for i in range(10):
    cars.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        race.print_status()

race.print_status()
print("\nRace finished!")
