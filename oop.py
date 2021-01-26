
class Animal:
    def __init__(self, eat, weight, voice, name):
        self.eat = eat  # кг
        self.weight = weight  # kg
        self.voice = voice
        self.name = name

    def eating(self, time):
        return self.eat * time    # кол-во еды * кол-во кормлений

    def weighing(self, new_weight):
        self.weight = new_weight     # новый вес после взвешивания


class Poultry(Animal):
    egg = 1

    def collect_eggs(self, quantity):
        return self.egg * quantity


class Cattle(Animal):
    milk = 0  # l

    def milking(self, time):
        return self.milk * time


class Geese(Poultry, Animal):
    voice = 'Quack'


class Cow(Cattle, Animal):
    voice = 'Muu'
    milk = 15


class Sheep(Animal):
    voice = 'Bee'
    wool = 15  # kg

    def hair_shearing(self, quantity):
        return self.wool * quantity


class Chicken(Poultry, Animal):
    voice = 'Co-co'

    def collecting_eggs(self, quantity):
        self.egg += quantity


class Goat(Cattle, Animal):
    voice = 'Mee'
    milk = 10


class Duck(Poultry, Animal):
    voice = 'Quack'


geese_one = Geese(1, 2, 'Кря', 'Серый')
geese_two = Geese(1, 2, 'Кря', 'Белый')

cow = Cow(10, 400, 'Мууу', 'Манька')

sheep_one = Sheep(7, 55, 'Бее', 'Барашек')
sheep_two = Sheep(6, 61, 'Бее', 'Кудрявый')

chicken_one = Chicken(2, 1, 'Кудах', 'Ко-Ко')
chicken_two = Chicken(2, 1, 'Кудах', 'Кукареку')

goat_one = Goat(3, 80, 'Мее', 'Рога')
goat_two = Goat(3, 90, 'Мее', 'Копыта')

duck = Duck(2, 3, 'Кря', 'Кряква')


animals_dict = {geese_one.name: geese_one.weight, geese_two.name: geese_two.weight, cow.name: cow.weight,
                sheep_one.name: sheep_one.weight, sheep_two.name: sheep_two.weight,
                chicken_one.name: chicken_one.weight, chicken_two.name: chicken_two.weight,
                goat_one.name: goat_one.weight, goat_two.name: goat_two.weight, duck.name: duck.weight}

count = 0
for weight_animal in animals_dict.values():
    count += weight_animal
print('Общий вес животных', count,  'килораммов')

max_count = 0
animal_id = 0
for i, y in animals_dict.items():
    if max_count < y:
        max_count = y
        animal_id = i
print(animal_id, 'самое тяжелое животное')


class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return "{} ({} мин.)".format(self.name, self.duration)

    def __repr__(self):
        return "{} ({} мин.)".format(self.name, self.duration)

    def show(self):
        #         print("Длинна песни:", self.duration, "мин.", "Название песни - ", self.name)
        return "<{}-{}>".format(self.name, self.duration)


class Album(Track):
    def __init__(self, album, group, tracks):
        self.album = album
        self.group = group
        self.tracks = tracks

    def add_track(self, name, duration):
        new_track = Track(name, duration)
        self.tracks.append(new_track)

    def get_info(self):
        return "Альбом: {}\nГруппа: {}\nТреки: {}".format(self.album, self.group, self.tracks)

    def get_tracks(self):
        tracks = []
        for track in self.tracks:
            tracks.append(track.show())
        return tracks

    #         return [track.show() for track in self.tracks]

    def get_duration(self):
        duration = 0
        for track in self.tracks:
            duration += track.duration
        return "{} мин.".format(duration)


#         return "{} мин.".format(sum([track.duration for track in self.tracks]))


track_1 = Track("Freedom", 3)
print(track_1.show())
track_2 = Track("everything", 2)
track_3 = Track("bomb", 4)

track_4 = Track("Job", 5)
track_5 = Track("ultra", 2)
track_6 = Track("great", 3)

# print()
# print(track_6)
# print()

album_1 = Album("Воздух", "Корни", [track_1, track_2, track_3])
album_2 = Album("Кислород", "Zazazy", [track_4, track_5, track_6])
print(album_1.get_info())
print(album_2.get_info())
# print(album_2.__dict__)

print(album_1.get_duration())
print(album_2.get_duration())

# print("Добавление трека в альбом 1")
# new_track_name = input("Введите название трека: ")
# new_track_duration = int(input("Введите длительность (десятичный формат): "))
# album_1.add_track(new_track_name, new_track_duration)

print(album_1.get_info())
print(album_1.get_duration())

print(album_1.get_tracks())
print()
print(album_2.get_tracks())











 















































