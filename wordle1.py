char_grey = input("введите серые буквы ")
char_yel = input("введите желтые буквы в формате: а1б2в3 ")
char_green = input("введите зеленые юуквы в формате: а1б2в3 ")

dop_word = []
alphabet = {chr(i) for i in range(1072, 1072 + 32)}
alphabet.difference_update({char for char in char_grey})

char_is = {}
char_is_set = set()
for i in range(0, len(char_yel), 2):
    k = int(char_yel[i+1])-1
    char_is_set.add(char_yel[i])
    if char_is.get(k):
        char_is[k].add(char_yel[i])
    else:
        char_is[k] = {char_yel[i]}

char_numb = {}
for i in range(0, len(char_green), 2):
    char_numb[int(char_green[i+1])-1] = char_green[i]

char = [0, 0, 0, 0, 0]
for i in range(5):
    char[i] = char_numb[i] if char_numb.get(i) else alphabet.difference(char_is.get(i) if char_is.get(i) else "")

f = open("C:\\Users\\Mike\\Desktop\\Russian_dictionary\\wordle_list.txt", "r")
for word in f:
    if word[0] in char[0] and word[1] in char[1] and word[2] in char[2] and word[3] in char[3] and word[4] in char[4]:
        dop_word.append(word[: 5])
f.close()
dop_word1 = []
for word in dop_word:
    flag = 1
    for char in char_is_set:
        if char not in word:
            flag = 0
    if flag:
        dop_word1.append(word)

for word in dop_word1:
    print(word)

