import codecs

L_W = 5
wordle_dic = set()
f = codecs.open("C:\\Users\\Mike\\Desktop\\Russian_dictionary\\singular.txt", encoding='utf-8')
for line in f:
    word = line[: -2].lower()
    if len(word) == L_W and word.isalpha():
        wordle_dic.add(word)
f.close()

alphabet = {chr(i): 0 for i in range(1072, 1072 + 32)}

for word in wordle_dic:
    for char in word:
        alphabet[char] += 1

# fa = open("C:\\Users\\Mike\\Desktop\\Russian_dictionary\\abc.txt", "w")
# for i in range(1072, 1072 + 32):
#
#     fa.write(chr(i) + ':' + str(alphabet[chr(i)]) + '\n')
# fa.close()

wordle_list = []
for word in wordle_dic:
    weight = 0
    for char in {char for char in word}:
        weight += alphabet[char]
    wordle_list.append([weight, word])

f = codecs.open("C:\\Users\\Mike\\Desktop\\Russian_dictionary\\singular_and_plural.txt", encoding='utf-8')
for line in f:
    word = line[: -2].lower()
    if len(word) == L_W and word.isalpha():
        if word not in wordle_dic:
            weight = 0
            for char in {char for char in word}:
                weight += alphabet[char]
            wordle_list.append([weight - 7000, word])
        wordle_dic.add(word)
f.close()
wordle_list.sort(reverse=True)

text = ""
for word in wordle_list:
    text += word[1] + " " + str(word[0]) + "\n"

fa = open("C:\\Users\\Mike\\Desktop\\Russian_dictionary\\wordle_list.txt", "w")
fa.write(text)
fa.close()

print("слов в словаре", len(wordle_dic))
