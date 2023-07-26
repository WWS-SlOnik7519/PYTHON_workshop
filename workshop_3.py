'''Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1'''

# import random
# from random import choice
#
# N = int(input("Введите число: "))
# count = 0
# list_A = [random.randint(1, N) for _ in range(N)]
# print(*list_A)
# x = choice(list_A)
# print(x)
# for i in list_A:
#     if i == x:
#         count += 1
# print(f'->', count)



'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5'''

# N = int(input("Введите число: "))
# list_A = [random.randint(1, N) for _ in range(N)]
# print(*list_A)
# x = choice(list_A)
# print(x)
#
# m = x
# res = 0
# result = list_A[0]
# for i in range(0, len(list_A)):
#     if list_A[i] != x:
#         res = abs(x - list_A[i])
#         if res <= m:
#             m = res
#             result = list_A[i]
# print(result)



'''Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12'''


# dict_scores = {1:'AEIOULNSTRАВЕИНОРСТ',
#                 2:'DGДКЛМПУ',
#                 3:'BCMPБГЁЬЯ',
#                 4:'FHVWYЙЫ',
#                 5:'KЖЗХЦЧ',
#                 8:'JXШЭЮ',
#                 10:'QZФЩЪ'}
# word = input('Введите слово: ').upper()
# score = 0
# for i in word:
#     for m, n in dict_scores.items():
#         if i in n:
#             score += m
# print('Стоимость слова:',score)


