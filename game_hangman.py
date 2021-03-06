# Создадите текстовую игру, классическую «Виселицу» .

# Правила:
# 1.Первый игрок загадывает слово и рисует черту для каждой буквы в этом
# слове (вы будете использовать нижнее подчеркивание ).
# 2.Второй игрок пытается отгадать слово по одной букве за раз.м
# 3.Если второй игрок правильно угадывает букву, первый игрок заменяет
# соответствующую черту этой правильной буквой. В данной версии игры,
# если буква встречается в слове дважды, ее нужно отгадать дважды.
# 4.Если второй игрок угадал неправильно, первый игрок рисует часть пове-
# шенной фигурки (начиная с головы).
# 5.Если второй игрок отгадывает все слово прежде, чем будет полностью
# нарисован висельник, он побеждает. Если нет, проигрывает.
#
# В нашей программе компьютер будет первым игроком, а отгадывающий че-
# ловек — вторым.

import random


def hangman(word):
    """
    wrong -счетчик неверных ответов.
    :param word: - слово которое нужно отгадать
    :return:
    """
    wrong = 0
    stages = ['',
              '____      ',
              '          ',
              '     |    ',
              '     O    ',
              '   / | \  ',
              '    / \   ',
              '          ',
              ]
    rletters = list(word)
    board = ['_']*len(word)
    win = False  # Меняется на 'True' в с случай победы.
    print('Добро пожаловать на казнь!')

    while wrong < len(stages) -1:
        print('\n')
        msg = 'Введите букву: '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[:e]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: ')
            print(' '.join(board))
            win = True
            break

    if not win:
        print('\n'.join(stages[:wrong]))
        print(f'Вы проиграли! Было загадано слово: {word}.')


a = ['кот', 'пес', 'лес', 'дом', 'пух', 'лом']
t = random.sample(range(len(a)-1), 1)[0]
hangman(a[t])
