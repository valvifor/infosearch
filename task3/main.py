# -*- codecs: utf-8 -*-
import codecs


def coder():
    input_file_name = input('Введите путь до файла, который надо зашифровать: ')
    input_file = codecs.open(input_file_name, 'r', "utf-8")
    text = input_file.read().lower()
    shift = input('Введите требуемый сдвиг: ')
    while not shift.isdigit():
        shift = input('Введено неверное значение! Введите требуемый сдвиг: ')
    shift = int(shift)
    language = input('Выберете язык (en/rus): ')
    while language != "en" and language != "rus":
        language = input('Введено неверное значение! Выберете язык (en/rus): ')

    if language == "en":
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    else:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alph_size = len(alphabet)
    coded_text = ''

    for i in text:
        new_index = (alphabet.find(i) + shift) % alph_size
        coded_text += alphabet[new_index]
    write_new_file(coded_text)


def write_new_file(text):
    output_file = codecs.open('output.txt', 'w', "utf-8")
    output_file.write(text)
    print('Текст зашифрован и сохранен в файле output.txt')


coder()
