brackets = {'()', '[]', '{}'}

line = input("Введите скобочную последовательность: ").replace(' ', '')
for i in range(int(len(line) / 2)):
    for j in brackets:
        line = line.replace(j, '')
if len(line) == 0:
    print('Правильная последовательность')
else:
     print('Неправильная последовательность')

