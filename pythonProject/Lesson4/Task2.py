from requests import get
import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp').text


def currency_rates(code):
    # поиск текущей даты
    begin_of_date = response.find('Date')
    day_1 = int(response[begin_of_date + 6:begin_of_date + 8])
    monyh_1 = int(response[begin_of_date + 9: begin_of_date + 11])
    year_1 = int(response[begin_of_date + 12: begin_of_date + 16])
    searchable_date = datetime.datetime(year=year_1, month=monyh_1, day=day_1)

    # зная структуру response, методом строк find, мы находим первое вхождение кода валюты в строку, и выводим
    # то что находится между срезами '<Value>' и '</Value>' , так как точно знаем, что между ними искомые данные
    searchable_code = response.find(code)
    if searchable_code == -1:
        return None
    else:
        begin_of_search = response.find('<Value>', searchable_code)
        end_of_search = response.find('</Value>', begin_of_search)
        print(searchable_date)  # вывод даты
        return float(response[begin_of_search + 7:end_of_search].replace(',',
                                                                         '.'))  # заменяем запятую на точку и приводим к float


# выводы возвращаемых значений для наглядности
print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('XXX'))
