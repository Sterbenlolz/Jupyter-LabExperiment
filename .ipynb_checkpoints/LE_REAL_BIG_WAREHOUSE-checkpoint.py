# Решил ввести схему закупки в компанию оборудования: сперва все попадает на склад, а потом уже оттуда сортируется
# по отделам. Соответственно нужна валидация на количество оборудования на складе, помимо общей валидации на, скажем,
# отсутствие букв в количестве и цене, на наличие отдела в компании и тд. Между отделами перемещений быть не может,
# все только через склад либо сразу на списание. Списание оборудования происходит добавлением его в отдельную таблицу,
# откуда оно уже никуда не девается. Кстати о таблицах: ради красивого оформления понадобилась новая библиотека.
# Класс склада здесь отвечает за отображение оборудования на местах в форме некоторой табличной отчетности и за
# перемещения оборудования внутри компании. И я не понял, о каких различиях между принтером, сканером и ксероксом
# помимо функционала может идти речь, но это ведь совершенно неважно, и поэтому я оставил только общие категории:
# название, тип, количество, цена. Для каждого отдела своя таблица в отчете!
from tabulate import tabulate


class Warehouse:
    department_list = ['Бухгалтерия', 'Производство', 'Колл-центр', 'HR', 'Склад', 'Списано']
    header = ['Название', 'Количество', 'Цена за штуку']
    accountance = [header]
    production = [header]
    callcentre = [header]
    HR = [header]
    warehouse = [header]
    writeoff = [header]
    count = 0

    @staticmethod
    def report():
        Warehouse.count += 1
        print('--------------------------------------------------------------')
        print(f'Отчет по оборудованию компании номер {Warehouse.count}')
        print(f'Оборудование в отделе: Бухгалтерия')
        if len(Warehouse.accountance) > 1:
            print(tabulate(Warehouse.accountance, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print('Оборудования нет.')
        print(f'Оборудование в отделе: Производство')
        if len(Warehouse.production) > 1:
            print(tabulate(Warehouse.production, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print('Оборудования нет.')
        print(f'Оборудование в отделе: Колл-центр')
        if len(Warehouse.callcentre) > 1:
            print(tabulate(Warehouse.callcentre, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print('Оборудования нет.')
        print(f'Оборудование в отделе: HR')
        if len(Warehouse.HR) > 1:
            print(tabulate(Warehouse.HR, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print('Оборудования нет.')
        print(f'Оборудование в отделе: Склад')
        if len(Warehouse.warehouse) > 1:
            print(tabulate(Warehouse.warehouse, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print('Оборудования нет.')
        print(f'Списанное оборудование: ')
        if len(Warehouse.writeoff) > 1:
            print(tabulate(Warehouse.writeoff, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print('Оборудования нет.')
        print('--------------------------------------------------------------')

    @staticmethod
    def distribute(name, department, amount):
        if str(amount).isdigit():
            print('Попытка доставки оборудования со склада в отдел...')
            num = 0
            departments = {'Бухгалтерия': Warehouse.accountance, 'Производство': Warehouse.production,
                           'Колл-центр': Warehouse.callcentre, 'HR': Warehouse.HR, 'Склад': Warehouse.warehouse,
                           'Списано': Warehouse.writeoff}
            for el in departments[department][:]:
                if name == el[0]:
                    p = el[-1]
                    a = el[-2]
                    departments[department].append([name, a + amount, p])
                    departments['Склад'].append([name, el[-2] - amount, el[-1]])
                    try:
                        departments[department].remove(el)
                        departments['Склад'].remove(el)
                    except ValueError:
                        pass
                else:
                    for elem in departments['Склад'][:]:
                        if name == elem[0]:
                            if elem[-2] > amount:
                                departments[department].append([name, amount, elem[-1]])
                                departments['Склад'].append([name, elem[-2] - amount, elem[-1]])
                                departments['Склад'].remove(elem)
                            elif elem[-2] == amount:
                                departments[department].append([name, amount, elem[-1]])
                                departments['Склад'].remove(elem)
                            else:
                                print('Ошибка: слишком много экземпляров заказано в отдел!')
                            num += 1
                    if num == 0:
                        print('Ошибка: такого оборудования нет на складе!')
        else:
            print('Ошибка: в графе Количество указано не число!')

    @staticmethod
    def write_off(name, department, amount):
        if str(amount).isdigit():
            print('Попытка списания оборудования...')
            num = 0
            departments = {'Бухгалтерия': Warehouse.accountance, 'Производство': Warehouse.production,
                           'Колл-центр': Warehouse.callcentre, 'HR': Warehouse.HR, 'Склад': Warehouse.warehouse,
                           'Списано': Warehouse.writeoff}
            for el in departments[department][:]:
                if name == el[0]:
                    p = el[-1]
                    a = el[-2]
                    if a > amount:
                        departments[department].append([name, a - amount, p])
                        departments['Списано'].append([name, amount, el[-1]])
                        departments[department].remove(el)
                    elif el[-2] == amount:
                        departments['Списано'].append([name, amount, el[-1]])
                        departments[department].remove(el)
                    else:
                        print('Ошибка: слишком много экземпляров отправлено на списание!')
                    num += 1
            if num == 0:
                print('Ошибка: такого оборудования нет на складе!')
        else:
            print('Ошибка: в графе Количество указано не число!')


class Printer:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        n = 0
        if str(self.amount).isdigit() and str(self.price).isdigit():
            print(
                f'Привет. Я новый принтер {self.name}, который заказан в количестве {self.amount} штук. Цена за экземпляр: {self.price}')
            for el in Warehouse.warehouse[:]:
                if self.name == el[0] and self.price == el[2]:
                    Warehouse.warehouse.append([el[0], amount + el[1], el[2]])
                    Warehouse.warehouse.remove(el)
                    n += 1
            if n == 0:
                printer_list = [self.name, self.amount, self.price]
                Warehouse.warehouse.append(printer_list)
        else:
            print('Ошибка: в графе Количество либо Цена указано не число!')


class Scanner:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        n = 0
        if str(self.amount).isdigit() and str(self.price).isdigit():
            print(
                f'Привет. Я новый сканер {self.name}, который заказан в количестве {self.amount} штук. Цена за экземпляр: {self.price}')
            for el in Warehouse.warehouse[:]:
                if self.name == el[0] and self.price == el[2]:
                    Warehouse.warehouse.append([el[0], amount + el[1], el[2]])
                    Warehouse.warehouse.remove(el)
                    n += 1
            if n == 0:
                scanner_list = [self.name, self.amount, self.price]
                Warehouse.warehouse.append(scanner_list)
        else:
            print('Ошибка: в графе Количество либо Цена указано не число!')


class Copier:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        n = 0
        if str(self.amount).isdigit() and str(self.price).isdigit():
            print(
            f'Привет. Я новый ксерокс {self.name}, который заказан в количестве {self.amount} штук. Цена за экземпляр: {self.price}')
            for el in Warehouse.warehouse[:]:
                if self.name == el[0] and self.price == el[2]:
                    Warehouse.warehouse.append([el[0], amount + el[1], el[2]])
                    Warehouse.warehouse.remove(el)
                    n += 1
            if n == 0:
                copier_list = [self.name, self.amount, self.price]
                Warehouse.warehouse.append(copier_list)
        else:
            print('Ошибка: в графе Количество либо Цена указано не число!')

p_1 = Printer('HP P3000', 2, 5389)
p_2 = Printer('HP P2000', 3, 3999)
s_1 = Scanner('Сanon DR-F180', 4, 2500)
s_2 = Scanner('Canon P215', 3, 3690)
c_1 = Copier('Xerox B205', 3, 10000)
c_2 = Copier('Xerox B215', 2, 12000)
Warehouse.report()
p_3 = Printer('HP P3000', 2, 5389)
s_3 = Scanner('blahblah', 'f', 23)
Warehouse.report()
Warehouse.distribute('HP P3000', 'Бухгалтерия', 2)
Warehouse.distribute('Canon P215', 'Колл-центр', 1)
Warehouse.report()
Warehouse.write_off('HP P3000', 'Бухгалтерия', 2)
Warehouse.report()
