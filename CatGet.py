class Cats:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.breed

    def get_age(self):
        return self.age

    def set_age(self):
        if age>0 and isinstance(age, int): #Проверка
            self.age = age
        else:
            print("Некорректная информация")