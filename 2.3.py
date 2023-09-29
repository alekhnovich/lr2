def f():
    n = int(input("Введите размер массива: "))
    arr = []
    for i in range(n):
        arr.append([0] * n)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i][j] = 1
            elif i < j:
                arr[i][j] = 0
            else:
                arr[i][j] = 2
    print("-----------")
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
    return arr


narr = f()