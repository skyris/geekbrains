#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import unittest
# from contextlib import contextmanager
# from io import StringIO


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License;)"

key = "ЗАБУЛДЫ"
file = "file0"
# with open(file, "r") as f:
#     text = f.read()
key = "БУЛКА"
text = "АДЦЕШБЮЩЬПЙДЛЬЕМШФФОУБЫЕЕОУТЕВБСЭЫЕВТМЕТПХУФАНЫВЬОВЖПЬОВОУЧЕУАУФАЛБОШЕЪШЮЧАТФЖЬАНЫЦТЦЙБШПРБАЛЩРЙЯРЪНЖЮЗСЯУШЪПРЭБЪТСБЕЗФАЛГЛЧЬЩШОШРПЧЩМОДБЬПГПЧШЙООЯУХИЧЫЩЧЕСУТКВУГЛСАГШПЭЮЪЫФШТЕШЦШМНЭЧЦОТЭЩМСЛБРФУРБЫШСОБРЦАТЮЩЙБЬЕЩМИЛБНЗТЙИШТКПЦПКНЖВЩЧИНУЦЦНЖЭЛСАМБЬЖВТШООАШЕЩБЕНЧЛХЬЩШЪТСБЕРХЬПЕМЕТБЕРЦООЮЮБШЖЯЩРЕУШЬХИИУАШЧЖЕУЛЫУБЪТСБЕЗЦНЖЭЛСАМБЬЖЧУБЬКМРЫЬКТЖЮЗЛЫУБНТКАХЦЙЕУДКФАУШОШРЙШФЛЫУУЪШДПФШШЙДБЫШДПХЩЦУЖЧУЧСУХРЧНПШВЬОРГУЫУЪШЪТСБЕРХЮСЫЬЭЮЪШЧЭБЬЕИЬООУЦТЧЙШНОУЩШРНООШХШТПГЩУДПЮУЭВЖГРЧНПДЭТЧУБПКНОБРЙВМШШТЕЖДЭЖНБДЛЦОНЧРХЕБАРЬОМПХШЕДБЪТСБЕРХЬТЭЩППСШПЫТБХЦПНЙШИЬОТБПЧОКДЭШРПАЖКСЕГЮНОКВУЫАУШЦЖНЖЧЩХЖЖАМЕТЭЭЛФФПЕЩНРБЗУЩРПДЭШПЖГРЧОТЫЭЖНБФЮЦАДЖЭШЧУБЩЧВЙЧУЬИТЮЖВИУБМЕКОБНПНООЧТГМУТКМЙЫЮВАНЫЬПЙШУЬЭНБДОШСРБПЫТГЖРЬИНШШЧОЮЕЩЩОТЮРОНЖШЦШЖОБРЩРЖЧЬЬАГЮРЧИЖЫЪШТПЯЮЦЫГЦЛСЕУУАМИЕЫЧЧЕГБТЦОЗАЖПДМТВЬЕОЫКШГСБЧЧЫЖЕЩБНЬШЩЬЧЖЕЖЛЕИХЬЙКПЬЪШПЬЕХТСПДЭШРПАЖЫАНБОШАГЕЩЪАНШСОУЖШЮНЛПХЖЦИХУХЬАНЫСТЗОЫЪЪОГШЬЬИТХЩИВПЮГПБОБЬШКСУДКЮЪЖЙОИБЦЩЧАМП"

letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

number_to_letter = dict(zip(range(len(letters)), letters))
encode_dict = {}
decode_dict = {}
for shift in range(len(letters)):
    """
    encode_dict[Буква шифра][Буква текста] -> Зашифрованная буква
    """
    encode_dict[number_to_letter[shift]] = dict(zip(letters, letters[shift:] + letters[:shift]))
    """
    decode_dict[Буква шифра][Зашифрованная буква] -> Буква текста
    """
    decode_dict[number_to_letter[shift]] = dict(zip(letters[shift:] + letters[:shift], letters))

# print(encode_dict)
# print(encode_dict["Б"]["З"])
# print(decode_dict["Б"][encode_dict["Б"]["З"]])

long_key = len(text)//len(key)*key + key[:len(text)%len(key)]
for k, el in zip(long_key, text):
    print( decode_dict[k][el], end="")
print("\n")
