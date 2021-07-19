print("Игра в крестики - нолики. \n"
      "Первым ходят крестики. \n")


def chislo(a):  # Проверка на число
    if a.isdigit():
        if int(a) in [i for i in range(1, 10)]:
            return int(a)
        else:
            print('Введите число от 1 до 9')
            return pole()
    else:
        print('Введите число от 1 до 9')
        return pole()


def zan(x, pol):  # Проверка на занятость ячейки
    if pol[x] == ' ':
        return x
    else:
        print("Ячейка занята, попробуйте снова!")
        return pole()


def pole():  # ход игрока
    a = input('Введите номер ячейки: ')
    return zan(chislo(a), P)


def win(w, pole):  # Условия победы
    if pole[1] == pole[2] == pole[3] == w or pole[4] == pole[5] == pole[6] == w or pole[7] == pole[8] == pole[9] == w:
        print(f'--------Победил {w}--------')
        print(f'   +---+---+---+\n'
              f'   | {P[1]}¹| {P[2]}²| {P[3]}³|\n'
              f'   +---+---+---+\n'
              f'   | {P[4]}⁴| {P[5]}⁵| {P[6]}⁶|\n'
              f'   +---+---+---+\n'
              f'   | {P[7]}⁷| {P[8]}⁸| {P[9]}⁹|\n'
              f'   +---+---+---+\n'
              f' ')
        return True
    if pole[1] == pole[4] == pole[7] == w or pole[2] == pole[5] == pole[8] == w or pole[3] == pole[6] == pole[9] == w:
        print(f'--------Победил {w}--------')
        print(f'   +---+---+---+\n'
              f'   | {P[1]}¹| {P[2]}²| {P[3]}³|\n'
              f'   +---+---+---+\n'
              f'   | {P[4]}⁴| {P[5]}⁵| {P[6]}⁶|\n'
              f'   +---+---+---+\n'
              f'   | {P[7]}⁷| {P[8]}⁸| {P[9]}⁹|\n'
              f'   +---+---+---+\n'
              f' ')
        return True
    if pole[1] == pole[5] == pole[9] == w or pole[7] == pole[5] == pole[3] == w:
        print(f'--------Победил {w}--------')
        print(f'   +---+---+---+\n'
              f'   | {P[1]}¹| {P[2]}²| {P[3]}³|\n'
              f'   +---+---+---+\n'
              f'   | {P[4]}⁴| {P[5]}⁵| {P[6]}⁶|\n'
              f'   +---+---+---+\n'
              f'   | {P[7]}⁷| {P[8]}⁸| {P[9]}⁹|\n'
              f'   +---+---+---+\n'
              f' ')
        return True


def game(P):  # Ход игры
    print(f'   +---+---+---+\n'
          f'   | {P[1]}¹| {P[2]}²| {P[3]}³|\n'
          f'   +---+---+---+\n'
          f'   | {P[4]}⁴| {P[5]}⁵| {P[6]}⁶|\n'
          f'   +---+---+---+\n'
          f'   | {P[7]}⁷| {P[8]}⁸| {P[9]}⁹|\n'
          f'   +---+---+---+\n'
          f' ')
    P[pole()] = "X"
    print(f'   +---+---+---+\n'
          f'   | {P[1]}¹| {P[2]}²| {P[3]}³|\n'
          f'   +---+---+---+\n'
          f'   | {P[4]}⁴| {P[5]}⁵| {P[6]}⁶|\n'
          f'   +---+---+---+\n'
          f'   | {P[7]}⁷| {P[8]}⁸| {P[9]}⁹|\n'
          f'   +---+---+---+\n'
          f' ')
    for i in range(4):
        print("Ходят 0")
        P[pole()] = "0"
        w = "0"
        if win(w, P):
            break
        print(f'   +---+---+---+\n'
              f'   | {P[1]}¹| {P[2]}²| {P[3]}³|\n'
              f'   +---+---+---+\n'
              f'   | {P[4]}⁴| {P[5]}⁵| {P[6]}⁶|\n'
              f'   +---+---+---+\n'
              f'   | {P[7]}⁷| {P[8]}⁸| {P[9]}⁹|\n'
              f'   +---+---+---+\n'
              f' ')
        print("Ходят Х")
        P[pole()] = "X"
        w = "X"
        if win(w, P):
            break
        print(f'   +---+---+---+\n'
              f'   | {P[1]}¹| {P[2]}²| {P[3]}³|\n'
              f'   +---+---+---+\n'
              f'   | {P[4]}⁴| {P[5]}⁵| {P[6]}⁶|\n'
              f'   +---+---+---+\n'
              f'   | {P[7]}⁷| {P[8]}⁸| {P[9]}⁹|\n'
              f'   +---+---+---+\n'
              f' ')
        if i == 3:
            print('----Ничья----')

    new_game()


def new_game():
    global P
    P = {i: ' ' for i in range(1, 10)}
    print("Сыграем еще раз? Y/N")
    if input() == 'Y':
        game(P)
    else:
        print("Спасибо за игру! До свидания!")
        input()


P = {i: ' ' for i in range(1, 10)}
game(P)