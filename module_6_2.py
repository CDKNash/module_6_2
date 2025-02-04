class Venicle:
    __COLOR_VARIANTS = ['Green', 'Brown', 'White', 'black']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            new_color is not self.__COLOR_VARIANTS
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Venicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Alesha', 'Vaz 2101', '60', 'Brown')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()