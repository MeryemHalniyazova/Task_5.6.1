adress = [i for i in range(1, 10)]

winnig_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def field():
    print(' ___________')
    for i in range(3):
        print('|', adress[0 + i * 3], '|', adress[1 + i * 3], '|', adress[2 + i * 3], '|')
    print(' ___________')


def moves(move):
    while True:
        value = int(input(move + ', please, enter the adress of your next move:'))

        if value not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            print('Wrong adress. Try again')
            continue
        if str(adress[value - 1]) in 'XO':
            print('This place is occupied. Try again!')
            continue
        adress[value - 1] = move
        print(adress, 'adress')
        break


def winnig():
    for i in winnig_combinations:
        if adress[i[0] - 1] == adress[i[1] - 1] == adress[i[2] - 1]:
            return adress[i[0] - 1]
    else:
        return False


def game():
    counter = 0
    while True:
        field()
        if counter % 2 == 0:
            moves('X')
        else:
            moves('O')
        if counter > 3:
            winner = winnig()
            if winner:
                field()
                print(winnig() + ' won!')
                break
        counter += 1
        if counter > 8:
            field()
            print('Draw!')
            break


game()
