class Car:
    def __init__(self, brand: str, model: str, year: int, color: str) -> None:
        """
        Инициализация автомобиля
         brand - Марка автомобиля
         model - Модель автомобиля
         year - Год выпуска автомобиля
         color - Цвет автомобиля
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def __str__(self) -> str:
        """
        Магический метод __str__, возвращает строку:
        "Марка модель, год выпуска, цвет".
        """
        return f"{self.brand} {self.model}, {self.year}, {self.color}"

    def __repr__(self) -> str:
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, color='{self.color}')"

    def drive(self) -> str:
        """
        Метод движения автомобиля
        """
        return f"{self.brand} {self.model} едет."

class PassengerCar(Car):
    """
    Класс для легковых автомобилей, дочерний класс
    seats - Количество мест
    """
    def __init__(self, brand: str, model: str, year: int, color: str, seats: int) -> None:
        """
        Инициализация легкового автомобиля
        brand - Марка автомобиля
        model - Модель автомобиля
        year - Год выпуска автомобиля
        color - Цвет автомобиля
        seats - Количество мест в автомобиле
        """
        super().__init__(brand, model, year, color)
        self.seats = seats

    def __str__(self) -> str:
        """
        Перегрузка магического метода __str__, возвращает строку:
        "Марка модель, год выпуска, цвет, количество мест"
        """
        return f"{super().__str__()}, {self.seats} мест."

    def drive(self) -> str:
        """
        Перегрузка метода drive
        "легковой автомобиль двигается быстрее, чем грузовой"
        """
        return f"{self.brand} {self.model} едет быстро."

class Truck(Car):
    """
    Класс для грузовых автомобилей
        payload_capacity - Грузоподъемность в тоннах
    """
    def __init__(self, brand: str, model: str, year: int, color: str, payload_capacity: float) -> None:
        """
        Инициализация грузового автомобиля
        brand - Марка автомобиля
        model - Модель автомобиля
        year - Год выпуска автомобиля
        color - Цвет автомобиля
        payload_capacity - Грузоподъемность в тоннах
        """
        super().__init__(brand, model, year, color)
        self._payload_capacity = payload_capacity

    def __str__(self) -> str:
        """
        Перегрузка __str__ для грузового автомобиля
        Перегрузка магического метода __str__, возвращает строку:
        "Марка модель, год выпуска, цвет, грузоподъемность"
        """
        return f"{super().__str__()}, {self._payload_capacity} тонн."

    def load(self, weight: float) -> str:
        """
        Метод загрузки груза
        weight - Вес груза в тоннах
        """
        if weight <= self._payload_capacity:
            return f"Груз в {weight} тонн успешно загружен в {self.brand} {self.model}."
        else:
            return f"Превышен лимит грузоподъемности! Максимальная грузоподъемность: {self._payload_capacity} тонн."

if __name__ == "__main__":
    car1 = PassengerCar("Toyota", "Mark II", 1990, "Чёрный", 5)
    car2 = Truck("Volvo", "FH16", 2022, "Синий", 20.0)

    print(car1)  # Используется метод __str__
    print(car1.drive())  # Используется метод drive()
    print(car2)  # Используется метод __str__
    print(car2.load(15))  # Используется метод load()