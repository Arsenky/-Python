class Date:
    string_date = ''
    day = 0
    month = 0
    year = 0

    def __init__(self, string_date):
        self.string_date = string_date

    @classmethod
    def convert_to_number(cls):
        cls.day = int(cls.string_date[:2])
        cls.month = int(cls.string_date[3:5])
        cls.year = int(cls.string_date[6:])

    @staticmethod
    def date_valid(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2022:
            print('Дата корректна')
        else:
            print('Дата не корректна')


Date.string_date = '10-02-2022'
Date.convert_to_number()
print(Date.day, Date.month, Date.year)
print(type(Date.day), type(Date.month), type(Date.year))
Date.date_valid(Date.day, Date.month, Date.year)
