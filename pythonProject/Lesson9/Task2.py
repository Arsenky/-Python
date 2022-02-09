class Road:
    _lenght = ()
    _widht = ()
    _mass = 25
    _lvl_widght = 0.05

    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht

    def cost_calc(self):
        return self._lenght * self._widht * self._mass * self._lvl_widght


Road1 = Road(20, 5000)
print(Road1.cost_calc())
