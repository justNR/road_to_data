# pylint: skip-file
"""
    Нужно реализовать надпись в формате "N просмотров". Падеж слова "просмотр" зависит
    от числа N. Например, 1 просмотр, 2 просмотра и т.п.
"""


def get_views_count(n: int) -> str:
    if n < 0:
        raise ValueError("Количество просмотров не может быть отрицательным")
    if not isinstance(n, int):
        raise ValueError("Количество просмотров должно быть целым числом")
    last_two_digit = n % 100
    if 11 <= last_two_digit <= 14:
       form = "просмотров"
    else:
        last_digit = n % 10
        if last_digit == 1:
            form = "просмотр"
        elif 2 <= last_digit <= 4:
            form = "просмотра"
        else:
            form = "просмотров"
    return f"{n} {form}"

"""
    Дан список, содержащий нули. Вернуть список, где все нули сдвинты вправо,
    сохранив порядок исходного списка:
    move_zeros([1, 0, 0, 2, 3, 0, 1]) -> [1, 2, 3, 1, 0, 0, 0]

    Решить в двух вариантах:
    - функция принимаем список и возвращает НОВЫЙ список
    - функция изменяет список, который был передан в аргументе функции 
    (функция ничего не возвращает)
"""


def move_zeros_with_new_dict(lst: list[float]) -> list:
    new_lst = [i for i in lst if i != 0]
    zeros = [0] * (len(lst) - len(new_lst))
    return new_lst + zeros

def move_zeros_two_pointers(lst: list[float]) -> None:
    slow = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[slow] = lst[i]
            slow +=1
    for j in range(slow, len(lst)):
        lst[j] = 0
    
        
"""
    Данные загрузились из БД с лишними символами, а должны быть только русские буквы.
    Напишите функцию, которая удаляет символы, которые не являются русскими буквами.
    "Иsвtrан Ив^%ан Ива?но)вич" -> "Иванов Иван Иванович"
"""


def clean_name(fio: str) -> str:
    res = []
    for ch in fio:
        if "А" <= ch <= "я" or ch in "Её":
            if ch.isspace():
                res.append(ch)
            res.append(ch)
    cleaned = ''.join(" ".join(res).split())
    return cleaned
print(clean_name("Иsвtrан Ив^%ан Ива?но)вич"))


"""
    Дан массив цен акций, вывести список, содержащий темпы прироста от периода к периоду.
    Для первого элемента списка выведите значение None. Округлите до целых.
    Например: [100, 150, 300, 400] -> [None, 50%, 100%, 33%]
"""


def get_pct_growth(s: list[float]) -> list[float]:
    grow_list = []
    grow_list.append(None)
    for i in range(1, len(s)):
        grow = (s[i] - s[i-1]) / s[i-1]
        grow = round(grow * 100)
        grow_list.append(grow)
    return grow_list
