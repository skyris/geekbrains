
text = "АДЦЕШБЮЩЬПЙДЛЬЕМШФФОУБЫЕЕОУТЕВБСЭЫЕВТМЕТПХУФАНЫВЬОВЖПЬОВОУЧЕУАУФАЛБОШЕЪШЮЧАТФЖЬАНЫЦТЦЙБШПРБАЛЩРЙЯРЪНЖЮЗСЯУШЪПРЭБЪТСБЕЗФАЛГЛЧЬЩШОШРПЧЩМОДБЬПГПЧШЙООЯУХИЧЫЩЧЕСУТКВУГЛСАГШПЭЮЪЫФШТЕШЦШМНЭЧЦОТЭЩМСЛБРФУРБЫШСОБРЦАТЮЩЙБЬЕЩМИЛБНЗТЙИШТКПЦПКНЖВЩЧИНУЦЦНЖЭЛСАМБЬЖВТШООАШЕЩБЕНЧЛХЬЩШЪТСБЕРХЬПЕМЕТБЕРЦООЮЮБШЖЯЩРЕУШЬХИИУАШЧЖЕУЛЫУБЪТСБЕЗЦНЖЭЛСАМБЬЖЧУБЬКМРЫЬКТЖЮЗЛЫУБНТКАХЦЙЕУДКФАУШОШРЙШФЛЫУУЪШДПФШШЙДБЫШДПХЩЦУЖЧУЧСУХРЧНПШВЬОРГУЫУЪШЪТСБЕРХЮСЫЬЭЮЪШЧЭБЬЕИЬООУЦТЧЙШНОУЩШРНООШХШТПГЩУДПЮУЭВЖГРЧНПДЭТЧУБПКНОБРЙВМШШТЕЖДЭЖНБДЛЦОНЧРХЕБАРЬОМПХШЕДБЪТСБЕРХЬТЭЩППСШПЫТБХЦПНЙШИЬОТБПЧОКДЭШРПАЖКСЕГЮНОКВУЫАУШЦЖНЖЧЩХЖЖАМЕТЭЭЛФФПЕЩНРБЗУЩРПДЭШПЖГРЧОТЫЭЖНБФЮЦАДЖЭШЧУБЩЧВЙЧУЬИТЮЖВИУБМЕКОБНПНООЧТГМУТКМЙЫЮВАНЫЬПЙШУЬЭНБДОШСРБПЫТГЖРЬИНШШЧОЮЕЩЩОТЮРОНЖШЦШЖОБРЩРЖЧЬЬАГЮРЧИЖЫЪШТПЯЮЦЫГЦЛСЕУУАМИЕЫЧЧЕГБТЦОЗАЖПДМТВЬЕОЫКШГСБЧЧЫЖЕЩБНЬШЩЬЧЖЕЖЛЕИХЬЙКПЬЪШПЬЕХТСПДЭШРПАЖЫАНБОШАГЕЩЪАНШСОУЖШЮНЛПХЖЦИХУХЬАНЫСТЗОЫЪЪОГШЬЬИТХЩИВПЮГПБОБЬШКСУДКЮЪЖЙОИБЦЩЧАМП"


num = 3

groups = [[]] * num

for i in range(len(text)):
    groups[i%num].append(text[i])



for i in range(num):
    for j in range(len(groups[i])):


print(groups)

open