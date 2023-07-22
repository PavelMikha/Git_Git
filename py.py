a = input()
n = a * 10
for i in range len(n):
    a += n
    if len(a) > 100:
        print('Al')
    else:
        print('vvvv')
