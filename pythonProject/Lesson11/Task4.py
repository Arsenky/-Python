class Warehouse:
    name = ''
    equipment_summ = 0
    equipment_list = []

    def __init__(self, name):
        self.name = name
        self.equipment_list = []

    def remove_equipment(self, equipment, new_warhouse):
        '''метод перемещает указанный экзэмпляр техники на указанный склад'''
        if equipment.warehouse_name != self.name:
            print(f'{equipment.model} нет на этом складе')
        else:
            self.equipment_summ -= 1
            equipment.warehouse_name = new_warhouse.name
            new_warhouse.equipment_summ += 1
            self.equipment_list.remove(equipment.model)
            new_warhouse.equipment_list.append(equipment.model)
            print(f'{equipment.model} перемещен на склад "{new_warhouse.name}"')

    def show_equipment_summ(self):
        '''выводит количество техники на складе'''
        print(f'Сейчас техники на скаладе "{self.name}": {self.equipment_summ}')

    def show_eqipment_list(self):
        '''выводит список техники на складе'''
        print(f'Cейчас на складе "{self.name}" следующая техника: {self.equipment_list}')


class OfficeEquipment:
    model = ''
    warehouse_name = ''
    count = 0
    price = 0

    def sent_to_warehouse(self, warehouse):
        '''метод определен перемещает экзэмпляр техники на указанный в водных данных склад'''
        if warehouse.name == self.warehouse_name:
            print(f'{self.model} уже на складе {warehouse.name}')
        else:
            warehouse.equipment_summ += 1
            self.warehouse_name = warehouse.name
            warehouse.equipment_list.append(self.model)
            print(f'{self.model} помещен на склад "{warehouse.name}"')


class Printer(OfficeEquipment):
    max_print_len = 0
    max_print_width = 0

    def __init__(self, model, price, max_prin_len, max_print_width):
        self.model = model
        self.price = price
        self.max_print_len = max_prin_len
        self.max_print_width = max_print_width
        Printer.count += 1


class Scaner(OfficeEquipment):
    resolution = []

    def __init__(self, model, price, resolution_x, resolution_y):
        self.model = model
        self.price = price
        self.resolution.append(resolution_x)
        self.resolution.append(resolution_y)
        Scaner.count += 1


warehouse1 = Warehouse('Основной')
warehouse2 = Warehouse('Запасной')
printer1 = Printer('NZ-100', 3000, 300, 180)
printer2 = Printer('LG-4561', 5000, 260, 120)
printer1.sent_to_warehouse(warehouse1)
warehouse1.show_equipment_summ()
printer2.sent_to_warehouse(warehouse1)
printer2.sent_to_warehouse(warehouse1)
warehouse1.show_equipment_summ()
warehouse1.show_eqipment_list()
warehouse2.show_eqipment_list()
warehouse1.remove_equipment(printer1, warehouse2)
warehouse1.show_equipment_summ()
warehouse2.show_equipment_summ()
warehouse1.show_eqipment_list()
warehouse2.show_eqipment_list()
