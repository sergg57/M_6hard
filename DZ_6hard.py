
class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=True):
        self.__sides = list(sides)  #self.__sides
        self.__color = color  #color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        if  len(sides) == self.sides_count:
            for i in range(len(sides)):
                if isinstance(sides[i], int):
                   continue
                else:
                    return False
            return True
        else:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)
            return False

    def get_sides(self):
        self.__is_valid_sides(self.__sides)
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = []
            for i in range(len(new_sides)):
                if isinstance(new_sides[i], int):
                    self.__sides.append(new_sides[i])
        else:
            return self.__sides

    def __len__(self):
        perimetr = 0
        for i in range(len(self.get_sides())):
            perimetr += self.get_sides()[i]
            #print(f'Периметр = {perimetr}')
        return perimetr


class Circle(Figure):
    sides_count = 1  #self.sides_count
    # def __init__(self, sides, color, filled):
    #     super().__init__(sides, color, filled)

    def get_radius(self):
        if len(self.get_sides()) == 1:
            self.__radius = self.get_sides()[0]/(2*3.14)
            return self.__radius
        else:
            self.__radius = 1/(2 * 3.14)
            return self.__radius

    def square(self):
        r = self.get_radius()
        return 3.14 * r**2


class Triangle(Figure):
    sides_count = 3
    # def __init__(self, sides, color, filled):
    #     super().__init__(sides, color, filled)

    def get_square(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5 # Формула Герона



class Cube(Figure):
    sides_count = 9
    # def __init__(self, sides, color, filled):
    #     super().__init__(sides, color, filled)

    def get_volume(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        return a * b * c


if __name__ == '__main__':

    circle1 = Circle((200, 200,100), color=[255, 0, 0], filled=True)
    print(f'Список сторон круга = {circle1.get_sides()}')
    print(f'Цвет круга = {circle1.get_color()}')
    print(f'Радиус круга = {circle1.get_radius()}')
    print(f'Площадь круга  = {circle1.square()}')
    print(f'Периметр круга = {circle1.__len__()}')

    circle1.set_sides(15)
    print(f'Список сторон круга = {circle1.get_sides()}')
    print(f'Радиус круга = {circle1.get_radius()}')
    print(f'Площадь круга  = {circle1.square()}')
    print(f'Периметр круга = {circle1.__len__()}')

    triangle1 = Triangle((200, 200, 200), color=[255, 0, 255], filled=True)
    print(f'Список сторон треугольника = {triangle1.get_sides()}')
    print(f'Цвет треугольника = {triangle1.get_color()}')
    print(f'Площадь треугольника = {triangle1.get_square()}')
    print(f'Периметр треугольника = {triangle1.__len__()}')

    triangle1.set_sides(15)
    print(f'Список сторон треугольника = {triangle1.get_sides()}')
    print(f'Площадь треугольника = {triangle1.get_square()}')
    print(f'Периметр треугольника = {triangle1.__len__()}')

    cube1 = Cube((200, 200, 100), color=[255, 255, 255], filled=True)
    print(f'Список сторон куба = {cube1.get_sides()}')
    print(f'Цвет куба = {cube1.get_color()}')
    print(f'Объем куба = {cube1.get_volume()}')
    print(f'Периметр куба = {cube1.__len__()}')

    cube1.set_sides(2, 2, 2, 2, 2, 2, 2, 2, 2)
    print(f'Список сторон куба = {cube1.get_sides()}')
    print(f'Объем куба = {cube1.get_volume()}')
    print(f'Периметр куба = {cube1.__len__()}')

