class Car:
    speed = 0
    name = ''
    color = ''
    is_polise = False

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, name, color):
        self.speed = speed
        self.color = color
        self.name = name

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Превышение скорости!')


class WorkCar(Car):
    def __init__(self, speed, name, color):
        self.speed = speed
        self.color = color
        self.name = name

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, name, color):
        self.speed = speed
        self.color = color
        self.name = name


class PoliceCar(Car):
    def __init__(self, speed, name, color):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = True


town_car = TownCar(70, 'Соседская машина', 'красный')
work_car = WorkCar(35, 'Экскаватор', 'желтый')
sport_car = SportCar(100, 'Ломбаргини', 'синий')
polic_car = PoliceCar(140, 'Полицейская машина', 'черный')

car_list = [town_car, work_car, sport_car, polic_car]
for car in car_list:
    print(car.name, car.color, car.is_polise)
    car.go()
    car.stop()
    car.turn('назад')
    car.show_speed()
    print()
