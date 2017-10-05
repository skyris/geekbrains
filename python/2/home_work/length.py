
text = "АДЦЕШБЮЩЬПЙДЛЬЕМШФФОУБЫЕЕОУТЕВБСЭЫЕВТМЕТПХУФАНЫВЬОВЖПЬОВОУЧЕУАУФАЛБОШЕЪШЮЧАТФЖЬАНЫЦТЦЙБШПРБАЛЩРЙЯРЪНЖЮЗСЯУШЪПРЭБЪТСБЕЗФАЛГЛЧЬЩШОШРПЧЩМОДБЬПГПЧШЙООЯУХИЧЫЩЧЕСУТКВУГЛСАГШПЭЮЪЫФШТЕШЦШМНЭЧЦОТЭЩМСЛБРФУРБЫШСОБРЦАТЮЩЙБЬЕЩМИЛБНЗТЙИШТКПЦПКНЖВЩЧИНУЦЦНЖЭЛСАМБЬЖВТШООАШЕЩБЕНЧЛХЬЩШЪТСБЕРХЬПЕМЕТБЕРЦООЮЮБШЖЯЩРЕУШЬХИИУАШЧЖЕУЛЫУБЪТСБЕЗЦНЖЭЛСАМБЬЖЧУБЬКМРЫЬКТЖЮЗЛЫУБНТКАХЦЙЕУДКФАУШОШРЙШФЛЫУУЪШДПФШШЙДБЫШДПХЩЦУЖЧУЧСУХРЧНПШВЬОРГУЫУЪШЪТСБЕРХЮСЫЬЭЮЪШЧЭБЬЕИЬООУЦТЧЙШНОУЩШРНООШХШТПГЩУДПЮУЭВЖГРЧНПДЭТЧУБПКНОБРЙВМШШТЕЖДЭЖНБДЛЦОНЧРХЕБАРЬОМПХШЕДБЪТСБЕРХЬТЭЩППСШПЫТБХЦПНЙШИЬОТБПЧОКДЭШРПАЖКСЕГЮНОКВУЫАУШЦЖНЖЧЩХЖЖАМЕТЭЭЛФФПЕЩНРБЗУЩРПДЭШПЖГРЧОТЫЭЖНБФЮЦАДЖЭШЧУБЩЧВЙЧУЬИТЮЖВИУБМЕКОБНПНООЧТГМУТКМЙЫЮВАНЫЬПЙШУЬЭНБДОШСРБПЫТГЖРЬИНШШЧОЮЕЩЩОТЮРОНЖШЦШЖОБРЩРЖЧЬЬАГЮРЧИЖЫЪШТПЯЮЦЫГЦЛСЕУУАМИЕЫЧЧЕГБТЦОЗАЖПДМТВЬЕОЫКШГСБЧЧЫЖЕЩБНЬШЩЬЧЖЕЖЛЕИХЬЙКПЬЪШПЬЕХТСПДЭШРПАЖЫАНБОШАГЕЩЪАНШСОУЖШЮНЛПХЖЦИХУХЬАНЫСТЗОЫЪЪОГШЬЬИТХЩИВПЮГПБОБЬШКСУДКЮЪЖЙОИБЦЩЧАМП"

original = "ЯСЛЫШАЛОТПИСАТЕЛЕЙКОТОРЫЕНАЗЫВАЮТСЕБЯБЫТОВИКАМИЧТОБУДТОБЫИНЕТНИКАКОГОЕЩЕУНАСБЫТАМИЛИЦИОНЕРАНАПРИМЕРНЕЛЬЗЯТЕПЕРЬОПИСАТЬКАКРАНЬШЕГОРОДОВОГОСЕГОДНЯОНМИЛИЦИОНЕРАЗАВТРАЗАВЕДУЮЩИЙОТДЕЛОММКММОСКОВСКОЕКУПОРОСНОЕМАСЛОЯБЫТОВИКОВЭТИХНИКОГДАНЕПОНИМАЛМНЕКАЗАЛОСЬВСЕГДАЧТОЧЕМДАЛЬШЕПИСАТЕЛЬОТБЫТАТЕМОНЛУЧШЕМОЖЕТЕСЛИЗАХОЧЕТИБЫТОПИСАТЬМНЕКАЗАЛОСЬЧТОСАМПИСАТЕЛЬБЫТОВИКЯВЛЯЕТСЯКАТЕГОРИЕЙБЫТАПОДОБНОЙГОРОДОВОМУЕДИНСТВЕННОЕЧТОПРИСУЩЕПИСАТЕЛЮРИСУЮЩЕМУБЫТЭТОНАЛИЧИЕВДУШЕЕГОНЕКОТОРОЙДОЛИУВЕРЕННОСТИЧТОДАННОЕЯВЛЕНИЕЕСТЬНАСАМОМДЕЛЕАНЕТОЛЬКОЕГОПИСАТЕЛЬСКОЕПРЕДСТАВЛЕНИЕЭТОСОДНОЙСТОРОНЫАСДРУГОЙПИСАТЕЛЬНЕДОЛЖЕНБЫТЬКАКФОТОГРАФИПРОСТОПЕРЕНОСИТЬНАБУМАГУТОЧТООНВИДИТИСЛЫШИТОБЫКНОВЕННЫМИГЛАЗАМИИУШАМИСЕЙЧАСУНАСГОСПОДСТВУЕТИМЕННОЭТОПОСЛЕДНЕЕЛОЖНОЕПРЕДСТАВЛЕНИЕИПОТОМУМЫВГАЗЕТАХВИДИМНЕВОЗМОЖНЫЕДЛЯЧТЕНИЯОГРОМНЫЕТОЧНЫЕОТЧЕТЫБЕЗВСЯКОЙПОПЫТКИСОСТОРОНЫСАМОГОАВТОРАМЕЖДУЕЕУГЛОВЫМИФАКТАМИЖИЗНИПРОВЕСТИСВОЮВОЛШЕБНОСОКРАЩАЮЩУЮДИАГОНАЛЬ"
# text = "ABCqywueorplj;fhsfvmn/k.,7;oprABC"

key = "ЗАБУЛДЫ"
long_key = len(text)//len(key)*key + key[:len(text)%len(key)]


d = {}
position = {}
full_len = len(text)
for length in range(3, full_len//2):
    added_flag = False
    for start in range(0, full_len-length+1):
        part = text[start:start+length]
        print(start, part)
        for place in range(start+length, full_len-length+1):
            if part == text[place:place+length]:
                d.setdefault(part, [])
                d[part].append(place-start)
                position.setdefault(part, [(start,start+length)])
                position[part].append((place, place+length))
                added_flag = True
    if not added_flag:
        break


straight_sec = sorted(d.keys(), key=len)
reversed_sec = sorted(d.keys(), key=len, reverse=True)
first = text.find(reversed_sec[0])
second = text.find(reversed_sec[0], text.find(reversed_sec[0])+1)
print("--->",first)
print("--->",second)
print(text[:first] +"__"+ text[first:second]+"__"+text[second:])
print(long_key[:first] +"__"+ long_key[first:second]+"__"+long_key[second:])
print(original[:first] +"__"+ original[first:second]+"__"+original[second:])

for k in reversed_sec:
    print(k, d[k])
print(len(key))

foo = lambda x: x/7
print("--------------------------------")
for k in reversed_sec:
    print(k, list(map(foo, d[k])))

import copy
new_d = copy.deepcopy(d)
print(new_d)
# TODO Убрать дублирования
# Если
# print("================================================")
new_sequence = []
len_dict = len(straight_sec)
# for i in range(len_dict):
#     item = straight_sec[i]
#     for i_curr in range(i+1, len_dict):
#         if straight_sec[i] in straight_sec[i_curr]:
#             if #Проверка что находится реально внутри
#                 pass
#             else:
#                 new_sequence.append(straight_sec[i])


#
#

print(position)
