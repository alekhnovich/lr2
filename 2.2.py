def count_characters(arg):
    if isinstance(arg, tuple):  # Если передан кортеж
        words = ' '.join(arg).split()  # Объединяем строки и разбиваем на слова
        return sum(len(word) for word in words)  # Суммируем длины всех слов
    elif isinstance(arg, list):  # Если передан список
        letters = sum(isinstance(item, str) for item in arg)  # Считаем количество строк в списке
        numbers = sum(isinstance(item, int) for item in arg)  # Считаем количество чисел в списке
        return letters, numbers
    elif isinstance(arg, int):  # Если передано число
        odd_digits = sum(int(digit) % 2 != 0 for digit in str(arg))  # Считаем количество нечетных цифр
        return odd_digits
    elif isinstance(arg, str):  # Если передана строка
        return len(arg)  # Считаем количество букв в строке
    else:
        return "Неподдерживаемый тип аргумента"

print("Сумма длин слов: ", count_characters(('hello', 'world')))
print("Количество букв в строке: ", count_characters("привет"))
print("Количество строк и чисел в списке: ", count_characters(['abc', 123, 'def', 456]))
print("Количество нечетных цифр: ", count_characters(13579))



