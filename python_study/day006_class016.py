class Circlecalculator(object):
    __PI = 3.14
    @staticmethod
    def calculate_area(radius):
        area = Circlecalculator.__PI * (radius **2)
        return round(area,2)

    @staticmethod
    def calculate_circumference(radius):
        circumference = 2 * Circlecalculator.__PI * radius
        return round(circumference,2)

if __name__ == "__main__":
    print("반지름:",3,"면적:",Circlecalculator.calculate_area(3))
    print("반지름:",3,"둘레:",Circlecalculator.calculate_circumference(3))