
# Модуль subprocess позволяет работать с процессами
from subprocess import Popen, CREATE_NEW_CONSOLE
import os

# Создаем кортеж расширений файлов, которые будут нужны
EXT = ('.py', '.PY')

# Создаем список файлов с нужным расширением в текущей директории
files = []
for f in os.listdir():
    if os.path.isfile(f) and f.endswith(EXT):
        files.append(f)

print(files)

# Для создания процесса используем класс Popen
# Будет создан процесс архиватора. 
# Флаг CREATE_NEW_CONSOLE укажет Popen создат новую консоль для процесса
packer = Popen('7z a test.zip {}'.format(' '.join(files)), creationflags=CREATE_NEW_CONSOLE)

# Ждём завершения процесса, чтобы что-то делать дальше...
packer.wait()

# Переименовываем файл, созданный архиватором
os.rename('test.zip', 'kolbasa.zzz')

