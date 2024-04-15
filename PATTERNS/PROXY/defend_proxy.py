class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(F"Car is begin driver by {self.driver.name}")


class CarProxy:
    """
    Это заместитель который импользуеться для управления доступом
    он добавляет различный функционал для контроля доступом!
    """
    def __init__(self, driver):
        self.driver = driver
        self.__car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self.__car.drive()
        else:
            print(F"Driver {self.driver.name} too young!!!")


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    driver = Driver('John', 12)
    car = CarProxy(driver)
    car.drive()
