# Подготовка файла со списком слов
my_file_word = open('russian_nouns.txt', "r", encoding='utf-8')
data_read = my_file_word.read()
list_noun = data_read.replace("\n", " ").split(" ")

# Распределение количесва слов по длине слов
dic_len_noun = {}
for i in list_noun:
    if len(i) not in dic_len_noun:
        dic_len_noun[len(i)] = 1
    else:
        dic_len_noun[len(i)] += 1
# Сортировка словаря по ключу
dic_len_noun = dict(sorted(dic_len_noun.items()))

print(f"Словарь содержит {len(list_noun)} слов", dic_len_noun)

len_word = int(input("Введите количество букв в слове: "))

# Отбор слов длиной {len_word} букв
list_noun_len = [i for i in list_noun if len(i) == len_word]

print(f"Всего слов из {len_word} букв:", len(list_noun_len))

# Поиск самых распространенных букв
d_word = {}
for i in list_noun_len:
    for j in i:
        if j not in d_word:
            d_word[j] = 1
        else:
            d_word[j] += 1
# Сортировка словаря по значению
d_word = dict(sorted(d_word.items(), key=lambda x: x[1], reverse=True))

print(f"Самые распространенные буквы в {len_word}-буквенных словах:")
print(d_word)

# Поиск количества букв на конкретном месте
arr = []
for number_char in range(len_word):
    d = {}
    for i in list_noun_len:
        if i[number_char] not in d:
            d[i[number_char]] = 1
        else:
            d[i[number_char]] += 1
    # Сортировка словаря по значению (по убыванию)
    d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    arr.append(d)

print(f"Самые распространенные буквы встречаются столько раз:")
for i in range(len_word):
    print(f"на {i + 1} месте: ", arr[i])
