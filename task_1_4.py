# Преобразовать слова «разработка», «администрирование»,
# «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).

a_str = ['разработка', 'администрирование', 'protocol', 'standard']
a_str_byte = []
a_str_decode = []

print(f'Начальное представление: \n {a_str}')
print()

for i in range(len(a_str)):
    a_str_byte.append(a_str[i].encode('utf-8'))
    a_str_decode.append(a_str_byte[i].decode('utf-8'))

print(f'Байтовое представление после кодировки: \n {a_str_byte}')
print()
print(f'Обратное преобразование с помощью декодировки: \n {a_str_decode}')
