class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        print('-' * 10)

    def text_in_line(self):
        print(' '.join(self.lyrics))

happy_bday = Song(["Не могу я тебе в день рождения",
                   "Дорогие подарки дарить,",
                   "Но зато в эти ночи весенние "])

bulls_on_parade = Song(["Далеко-далеко на лугу пасется кто?",
                        "Пейте, дети, молоко, будете здоровы!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


first_poem = ["В блеске огней, за зеркальными стеклами," ,"Пышно цветут дорогие цветы,", "Нежны и сладки их тонкие запахи,", "Листья и стебли полны красоты."]

second_text = ["Every time Im walking by your house", "I stop and I feel you looking down", "I thought I heard a whisper in the breeze"]

poem_bunin = Song(first_poem)

text = Song(second_text)

# poem_bunin = Song(["В блеске огней, за зеркальными стеклами,",
#                    "Пышно цветут дорогие цветы,",
#                    "Нежны и сладки их тонкие запахи,",
#                    "Листья и стебли полны красоты."])
#
# text = Song(["Every time Im walking by your house",
#              "I stop and I feel you looking down",
#              "I thought I heard a whisper in the breeze"])

poem_bunin.sing_me_a_song()

text.sing_me_a_song()

poem_bunin.text_in_line()
