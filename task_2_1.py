import re
import csv


def get_data(f_name):
    my_list = ['' for i in enumerate(my_patt)]
    with open(f_name) as f_n:
        for row in f_n:
            for i, my_val in enumerate(my_patt):
                my_math = re.search(my_val, row)
                if my_math:
                    my_list[i] = row.split(sep=':')[1].strip()
    return my_list


def write_to_csv(f_name):
    my_find_list = []
    for i in range(1, 4):
        my_f_name = f'info_{str(i)}.txt'
        my_find_list.append(get_data(my_f_name))

    with open(f_name, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        f_n_writer.writerow(my_patt)
        f_n_writer.writerows(my_find_list)


my_patt = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
write_to_csv('main_data.csv')

with open('main_data.csv') as f_n:
    print(f_n.read())
