# Создаем карточную игру «Пьяница». В этой игре каждый игрок берет из колоды по карте — побеждает тот,
# у которого карта старше. При создании игры вы будете определять классы, представляющие карту, колоду,
# игрока и, наконец, саму игру.

from random import shuffle


class Card:
    """
    suits - масти карт.
    values - номинал карт.
    """
    # Масти находятся по возрастанию чем выше индекс масти тем она сильнее.
    suits = ['пик', 'черви', 'бубны', 'треф']
    # Добавляем вначало два None чтобы индексы совпадали с номиналом карт.
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

    def __init__(self, value, suit):
        """value и suit целые числа."""
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return self.values[self.value] + ' ' + self.suits[self.suit]


class Deck:
    def __init__(self):
        """Функция которая создает колоду и перемешивает."""
        self.cards = []  # Создаем колоду.
        for i in range(2, 15):  # Определяем карту.
            for j in range(4):  # Определяем масть.
                self.cards.append(Card(i, j))  # Наполняем колоду.
        shuffle(self.cards)  # Перемешываем колоду.

    def remove_card(self):
        """Метод который выдает по одной карте из колоды."""
        if len(self.cards) == 0:  # Если в коложе нет карт возвращаем None.
            return
        return self.cards.pop()  # Если карты есть возвращаем последнюю и затем удаляем ее из колоды.


class Player:
    """Класс игрок. Отслеживаем: карты игрока и отслеживать количество выигранных ими раундов()."""

    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input('имя первого играка: ')
        name2 = input('имя второго играка: ')
        self.deck = Deck()  # создаем новый обьект Deck сохраняя его в переменную экземпляра класса deck
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        """Метод начинает игру, игра продожается пока в колоде две или больше двух карт или пока пользователь не нажмет 'X'"""
        cards = self.deck.cards  # мы можем вызывать deck с маленькой так как выше мы вызов класса присвоели.
        print('Поехали!')
        while len(cards) >= 2:
            response = input('Нажмите X для выхода. Нажмите любую другую клавишу для начала игры.')
            if response.upper() == 'X':
                break
            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()

            print("{} кладет {}, а {} кладет {}.".format(self.player1.name, player1_card, self.player2.name,
                                                         player2_card))
            if player1_card > player2_card:  # сравниваем карты
                self.player1.wins += 1
                print("{} забирает карты".format(self.player1.name))
            else:
                self.player2.wins += 1
                print("{} забирает карты".format(self.player2.name))

        print("Игра окончена. {} выиграл!".format(self.winner(self.player1, self.player2)))

    def winner(self, player1, player2):
        """Метод который подсчитывает выиграные раунды и возвращает игрока который победил."""
        if player1.wins > player2.wins:
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return 'Ничья!'


game = Game()
game.play_game()
