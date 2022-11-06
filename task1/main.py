def input_validation():
    n = input("Введите количество строк для треугольника Паскаля: ")
    while n == '0' or not n.isdigit():
        n = input("Введено неверное значение! Введите целое положительное число: ")
    return int(n)


def Pascal_triangle(n):
    print("Первые " + str(n) + " строк треугольника Паскаля:")
    triangle = []
    for i in range(n):
        line = [1] * (i + 1)
        for j in range(1, i):
            line[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(line)
        print(triangle[i])


n = input_validation()
Pascal_triangle(n)
