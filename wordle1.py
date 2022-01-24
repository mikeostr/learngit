char_grey = input("введите серые буквы в формате абв")
char_yel = input("введите желтые буквы в формате: а1б2в3 ")
char_green = input("введите зеленые буквы в формате: а1б2в3 ")

alphabet = {chr(i) for i in range(1072, 1072 + 32)}
alphabet.difference_update({char for char in char_grey})

char_is = dict()
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

char = list(range(5))
for i in range(5):
    char[i] = char_numb[i] if char_numb.get(i) else alphabet.difference(char_is.get(i) if char_is.get(i) else "")

allowed_words = []
f = open("C:\\Users\\Mike\\Desktop\\Russian_dictionary\\wordle_list.txt", "r")
for word in f:
    if all(word[i] in char[i] for i in range(5)):
        if all(char in word for char in char_is_set):
            allowed_words.append(word[: 5])
f.close()

for word in allowed_words:
    print(word)
