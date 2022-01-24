dop_word = []
char_no = "сприкон"  # grey and green
char_is = "ае"  # yellow
alphabet = {chr(i) for i in range(1072, 1072 + 32)}
for char in char_no:
    alphabet.remove(char)

f = open("C:\\Users\\Mike\\Desktop\\Russian_dictionary\\wordle_list.txt", "r")
for word in f:
    char0 = alphabet.difference("")  # "yellow" or {green}
    char1 = alphabet.difference("а")  # "yellow" or {green}
    char2 = alphabet.difference("")  # "yellow" or {green}
    char3 = alphabet.difference("")  # "yellow" or {green}
    char4 = {"р"}  # alphabet.difference("а")  # "yellow" or {green}
    if word[0] in char0 and word[1] in char1 and word[2] in char2 and word[3] in char3 and word[4] in char4:
        dop_word.append(word[: 5])
f.close()
dop_word1 = []
for word in dop_word:
    flag = 1
    for char in char_is:
        if char not in word:
            flag = 0
    if flag:
        dop_word1.append(word)

for word in dop_word1:
    print(word)

