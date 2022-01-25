import codecs

L_W = 5
wordle_dic = {}
f = codecs.open("C:\\Users\\Mike\\Desktop\\Russian_dictionary\\singular.txt", encoding='utf-8')
for line in f:
    line = line[: -2]
    if len(line) == L_W and line.isalpha():
        wordle_dic[line] = 0
f.close()

alphabet = {chr(i): 0 for i in range(1072, 1072 + 32)}

for word in wordle_dic:
    for char in word:
        alphabet[char] += 1

wordle_list = []
for word in wordle_dic:
    weight = 0
    for char in {char for char in word}:
        weight += alphabet[char]
    wordle_dic[word] = weight
    wordle_list.append([weight, word])
wordle_list.sort(reverse=True)

text = ""
for word in wordle_list:
    text = text + word[1] + " " + str(word[0]) + "\n"

fa = open("C:\\Users\\Mike\\Desktop\\Russian_dictionary\\wordle_list.txt", "w")
fa.write(text)
fa.close()

print("слов в словаре", len(wordle_dic))
