print('Добро пожаловать в игру " Крестики - нолики"' )
print('_________________________________')
print('Правила игры - нужно ввести 2 координаты')
print('Первая координата - номер строки')
print('Вторая координата - номер столбца')
print('_________________________________')


#создаем игровое поле

Fb=[["_"]*3,["_"]*3,["_"]*3]#переменная поля
def Bdcr():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {Fb[i][0]} {Fb[i][1]} {Fb[i][2]}")
Bdcr()
print("Hачинают X")


def input_XxO():
    while True:
        cords = input("         Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Введите числа от 0 до 2! ")
            continue
        if Fb[x][y] != "_":
            print(" Уже занята! ")
            continue
        return x,y
def Win_check(): # функция проверки выигрышных комбинаций
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win:
        symvol = []
        for c in cord:
            symvol.append(Fb[c[0]][c[1]])
        if symvol == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symvol == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

x,y=input_XxO()
count=0
while True:
    count += 1
    print (f"  0 1 2" )
    for i in range(3):
        print(f"{i} {Fb[i][0]} {Fb[i][1]} {Fb[i][2]}")
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    x, y = input_XxO()
    if count % 2 == 1:
        Fb[x][y] = "X"
    else:
        Fb[x][y] = "0"
    if Win_check():
        break
    if count == 9:
        print(" Нет победителя!")
        break