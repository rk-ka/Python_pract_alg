
""" Инкапсуляция.
    Чтобы все функции, отн. к одному объекту (Dragon)
    находились в одном месте, объединям их в класс.
    На первом месте в аргументах фун. всегда - self ("Я"),
    это означает что функции работают только с объектами данного класса.

    """


class Dragon:
    
    def __init__(self, name):
        #инициализ. объект с обязательными св-ми класса
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0 #True/False

    def get_damage(self, damage):
        self.health #TO FIX
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def talk(self):
        print(self.name, "health", self.health, ". Hit me!")

    def final_cry(self):
        print(self.name, 'is dead...')


def main():
    enemy_list = [Dragon('Smog'), Dragon('Hidra'), Dragon('Vasil')]
    finish = False
    while not finish:
        enemy = enemy_list[0]
        enemy.talk()
        damage = int(input())
        enemy.get_damage(damage)
        if not enemy.is_alive(): #удалить из списка мертвого врага
            enemy.final_cry()
            enemy_list.pop(0)
        if not enemy_list: #если список пуст (not True)
            finish = True
    print("You WIN!")



main()
