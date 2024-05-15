class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1000000

    def horse_powers(self):
        return 'количество лошадиных сил'


class Nissan(Car, Vehicle):
    price = 2000000
    vehicle_type = 'sedan'

    def horse_powers(self):
        print('количество лошадиных сил 150')


n = Nissan()
print(n.vehicle_type)
print(n.price)
Nissan.horse_powers(n)
