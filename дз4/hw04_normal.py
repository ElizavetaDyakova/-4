# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    f = 1 # начальное значение первого элемента
    a = 1 #начальное значение второго элемента
    q = 2 #номер элемента
    #Функция построения ряда Фибоначчи
    for q in range(q, m):
        f = f + a
        a = f - a
        q += 1
        if q >= n:
            print(f)
        else:
            continue
#вывод
print(fibonacci(10, 20))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        #функция сортирвки
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list
#вывод
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


strok = [2, 'adfgd', 2, 5, 6,'sget'] #строка
func = lambda x: type(x) == str #функция для проверки соответствия типа элемента строке
#функция фильтр
def filter(func, strok):
    output_str = [] #создаем список
    for i in range(len(strok)):
        if func(strok[i]) == True:
            output_str.append(strok[i])
    return output_str


print(filter(func, strok)) #вывод


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

