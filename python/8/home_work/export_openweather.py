
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sys

if len(sys.argv) != 4:
    print("Введите запрос в правильном формате:\n")
    print("export_openweather.py --csv filename [<город>]\n" \
            "export_openweather.py --json filename [<город>]\n" \
            "export_openweather.py --html filename [<город>]\n")
    sys.exit()

output_format, file, city = sys.argv[1:]

print(output_format)
print(file)
print(city)