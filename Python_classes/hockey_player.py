class HockeyPlayer:
    # Атрибуты класса
    default_position = "Forward"

    # Конструктор класса
    def __init__(self, name, surname, age, team):
        # Атрибуты экземпляра
        self.name = name
        self.surname = surname
        self.age = age
        self.team = team

    # Метод экземпляра
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    
    # Метод класса (объявляется с помощью декоратора @classmethod)
    @classmethod
    def get_default_position(cls):
        return cls.default_position
    
    # Статический метод (объявляется с помощью декоратора @staticmethod).
    # Его можно воспринимать как метод, который «не знает к какому классу он относится».
    # Используется обычно как вспомогательная функция и работает с данными, которые им не переданы
    @staticmethod
    def get_greeting():
        return "Привет, хоккеист!"

    # Свойство - метод, работа с которым подобна работе с атрибутом (объявляется 
    # с помощью декоратора @property). Изменить значение этого свойства снаружи
    # не получится, однако, это возможно.
    @property
    def is_lucky(self):
        return len(self.name + self.surname) == self.age
    
class HokeyPlayerPlus(HockeyPlayer):
    default_position = 'Reserver forward'

    def is_lucky(self):
        if self.age < 18:
            return True
        return super().is_lucky()
    

player_1 = HokeyPlayerPlus("Степан", "Осечкин", 17, "Питония Де ТуДуй")

print(player_1.is_lucky())