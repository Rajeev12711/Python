class Car:
    def __init__(self, **kw):
        self.color = kw.get('color')
        self.year = kw.get('year')
        self.model = kw.get('model')
        self.company = kw.get('company')

my_car =Car(color= 'red', year=2020)
print(my_car.color)
print(my_car.company)