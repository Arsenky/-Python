import time


class TrafficLight:
    _text = '***\n*****\n*****\n*****\n ***\n'
    _color = 'None'

    def running(self, color):
        self._color = color
        if self._color == 'red':
            print(f'\033[31m {self._text}')
            time.sleep(7)
        elif self._color == 'green':
            print(f'\033[32m {self._text}')
            time.sleep(8)
        elif self._color == 'yellow':
            print(f'\033[33m {self._text}')
            time.sleep(2)
        else:
            print('некорректный цвет')


TrafficLight1 = TrafficLight()
TrafficLight1.running('red')
TrafficLight1.running('green')
TrafficLight1.running('yellow')
