class Dessert:
    """
        >>> print("Dessert1 это " + str(dessert1.name))
        Dessert1 это Meringue
        >>> print("Калорийность " + str(dessert1.name) + ' - ' + str(dessert1.calories))
        Калорийность Meringue - 234
        >>> print("Это полезный десерт? " + str(dessert1.is_healthy()))
        Это полезный десерт? False
        >>> print("Это вкусный десерт? " + str(dessert1.is_delicious()))
        Это вкусный десерт? True
        >>> print("Dessert2 это " + str(dessert2.name))
        Dessert2 это Waffles
        >>> print("Калорийность " + str(dessert2.name) + ' - ' + str(dessert2.calories))
        Калорийность Waffles - 200
        >>> print("Это полезный десерт? " + str(dessert2.is_healthy()))
        Это полезный десерт? False
        >>> print("Это вкусный десерт? " + str(dessert2.is_delicious()))
        Это вкусный десерт? True
        >>> print("Вкус - " + str(dessert2.flavor))
        Вкус - yummy
        >>> print("Dessert3 is " + str(dessert3.name))
        Dessert3 is Cherry jelly
        >>> print("Калорийность " + str(dessert3.name) + ' - ' + str(dessert3.calories))
        Калорийность Cherry jelly - 80
        >>> print("Это полезный десерт? " + str(dessert3.is_healthy()))
        Это полезный десерт? True
        >>> print("Это вкусный десерт? " + str(dessert3.is_delicious()))
        Это вкусный десерт? False
        >>> print("Вкус - " + str(dessert3.flavor))
        Вкус - black licorice
    """

    def __init__(self, name="nameless", calories=0):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @property
    def calories(self):
        return self._calories

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @calories.setter
    def calories(self, new_calories):
        self._calories = new_calories

    def is_healthy(self):
        if self._calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    "Класс для проверки вкуса десерта"

    def __init__(self, name="nameless", calories=0, flavor='unknown'):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, new_flavor):
        self._flavor = new_flavor

    def is_delicious(self):
        if self._flavor == 'black licorice':
            return False
        else:
            return True


# Тесты
dessert1 = Dessert(calories=234)
dessert1.name = 'Meringue'

dessert2 = Dessert('Waffles')
dessert2.flavor = 'yummy'
dessert2.calories = 200

dessert3 = JellyBean('Jelly', 80, 'black licorice')
dessert3.name = 'Cherry jelly'

dessert = JellyBean()
