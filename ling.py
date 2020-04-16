def pointscounter(string):
    final = string.count('.') + string.count('?') + string.count('!')
    return final

def lettercounter(string):
    letters = 'ЁУЕЫАОЭЯИЮуеыаоэяиюёaeuioy'
    final = 0
    for l in letters:
        final += string.count(l)
    return final

def wordscounter(string):
    return string.count(' ') + 1 - string.count(' - ')

def main():
    string = input()
    points = pointscounter(string)
    letters = lettercounter(string)
    words = wordscounter(string)
    ASL = words / points
    ASW = letters / words
    FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)

    print('Предложений: ', points)
    print('Слов: ', words)
    print('Слогов: ', letters)
    print('Средняя длина предложения в словах: ', ASL)
    print('Средняя длина слова в слогах: ', ASW)
    print('Индекс удобочитаемости Флеша: ', FRE)
    if FRE > 80:
        print('Текст очень легко читается (для младших школьников).')
    elif 80 >= FRE > 50:
        print('	Простой текст (для школьников).')
    elif 50 >= FRE > 20:
        print('	Текст немного трудно читать (для студентов).')
    else:
        print('Текст трудно читается (для выпускников ВУЗов).')


if __name__ == '__main__':
    main()