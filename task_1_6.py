# Создать текстовый файл test_file.txt, заполнить его
# тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

my_file = open('test_file.txt', 'w')
my_file.writelines('сетевое программирование\n')
my_file.writelines('сокет\n')
my_file.writelines('декоратор\n')
my_file.close()

print(my_file)
print()

with open('test_file.txt', encoding='utf-8') as my_file:
    for line in my_file:
        print(line, end= '')

