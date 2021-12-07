"""парсиг файла mts*.txt на рабочем столе для подсчета трафика мтс. входящие и исходящие звонки не различает
СМС не обрабатывает"""


f = open("C:\\Users\\Mike\\Desktop\\mts1.txt", 'r')
tex = []
for line in f:
    tex.append(line.split("\t"))
f.close()

s = 0 # ammaunt traffic
inter, talk = [], []
# цикл просмотра текста, разбор каждой строки, перевод трафика в кБ,
for i in range(len(tex)//2):
    year, month, day, time = tex[2*i][0][6:10], tex[2*i][0][3:5], tex[2*i][0][:2], tex[2*i][0][-5:]
    tipe = tex[2*i][1]
    if tipe == 'Интернет':
        aid = tex[2*i][2]
        traf = tex[2*i][3][: -2].replace(',', '.').replace(' ', '')
        traf = 0 if traf == '1ш' else float(traf)
        multiplier = tex[2*i][3][-2:]
        if multiplier == 'Мб':
            traf *= 1024
        elif multiplier == 'Гб':
            traf *= 1024 ** 2

        s += traf
        many = tex[2*i+1][0].split()[0]
        inter.append([year, month, day, aid, traf, many])
    elif tipe == 'Звонки':
        aid = tex[2*i][2]
        duration = tex[2*i][3]
        many = tex[2 * i + 1][0].split()[0]
        talk.append([year, month, day, aid, duration, many])
print("All traffic=", s / 1024 / 1024, "Gb")
tipe_aid = {}  # цель трафика: трафик
day_inter = {}  # словарь день: трафик

for line in inter:
    if line[3] in tipe_aid:
        tipe_aid[line[3]] += line[4]
    else:
        tipe_aid[line[3]] = line[4]
    date = '.'.join(line[:3])
    if date in day_inter:
        day_inter[date] += line[4]
    else:
        day_inter[date] = line[4]
for i in tipe_aid:
    print(i, tipe_aid[i] // 1024, "Mb")
traf_day = []
s = 0
for day in day_inter:
    traf_day.append([int(day_inter[day]/1024), day])
    s += day_inter[day]
traf_day.sort(reverse=True)
for i in traf_day:
    print(i[1], '     ', i[0], 'Mb')


duration, duration_s = 0, 0
many = 0
for line in talk:
    dur_ms = line[4].split('.')
    if len(dur_ms) > 2:
        second = int(dur_ms[1].split()[0])
    else:
        second = 0
    minutes = int(dur_ms[0].split()[0])
    duration += minutes
    duration_s += second
    many += int(line[5])
duration = duration + duration_s // 60
duration_s = duration_s % 60
print(duration, 'min', duration_s, 'sec', many, 'rub')
