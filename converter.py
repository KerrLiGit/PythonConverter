"""Основной модуль программы."""


from prac3.converters import Weight, Pressure, Length

if __name__ == '__main__':
    print('1 - Length\n2 - Pressure\n3 - Weight')
    while True:
        print('Выберите номер класса: ')
        val = int(input())
        if val <= 0 or val >= 6:
            break
        if val == 1:
            print('1 - meters_to_inch\n2 - kilometers_to_mile'
                  '\n3 - meters_to_yard\n4 - meters_to_foots\n5 - '
                  'kilometers_to_sea_mile')
            print('Номер операции: ')
            method = int(input())
            print('Введите значение: ')
            if method <= 0 or method >= 6:
                break
            if method == 1:
                print('Метры в дюймы: ' + str(
                    Length.Length.meters_to_inch(None, float(input()))))
            if method == 2:
                print('Километры в мили: ' + str(
                    Length.Length.kilometers_to_mile(None, float(input()))))
            if method == 3:
                print('Метры в ярды: ' + str(
                    Length.Length.meters_to_yard(None, float(input()))))
            if method == 4:
                print('Метры в футы: ' + str(
                    Length.Length.meters_to_foots(None, float(input()))))
            if method == 5:
                print('Метры в морские мили: ' + str(
                    Length.Length.kilometers_to_sea_mile(
                        None, float(input()))))
        if val == 2:
            print('1 - bar_to_atmosphere\n2 - bar_to_pascal'
                  '\n3 - atmosphere_to_torr')
            print('Выберите номер операции: ')
            method = int(input())
            print('Введите значение: ')
            if method <= 0 or method >= 4:
                break
            if method == 1:
                print('Бары в атмосферы: ' + str(
                    Pressure.Pressure.bar_to_atmosphere(None, float(input()))))
            if method == 2:
                print('Бары в паскали: ' + str(
                    Pressure.Pressure.bar_to_pascal(None, float(input()))))
            if method == 3:
                print('Атмосферы в торры: ' + str(
                    Pressure.Pressure.atmosphere_to_torr(
                        None, float(input()))))
        if val == 3:
            print('1 - ton_to_english_ton\n2 - ton_to_american_ton'
                  '\n3 - kilogram_to_lb\n4 - kilogram_to_ounce')
            print('Номер операции: ')
            method = int(input())
            print('Введите значение: ')
            if method <= 0 or method >= 5:
                break
            if method == 1:
                print('Тонны в английские тонны: ' + str(
                    Weight.Weight.ton_to_english_ton(None, float(input()))))
            if method == 2:
                print('Тонны в американские тонны: ' + str(
                    Weight.Weight.ton_to_american_ton(None, float(input()))))
            if method == 3:
                print('Килограммы в фунты: ' + str(
                    Weight.Weight.kilogram_to_lb(None, float(input()))))
            if method == 4:
                print('Килограммы в унции: ' + str(
                    Weight.Weight.kilogram_to_ounce(None, float(input()))))
