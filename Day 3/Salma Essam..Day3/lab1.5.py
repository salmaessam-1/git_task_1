##Write a program that build a Mario pyramid

def py(num):
    num = int(num)
    for i in range(1, num + 1):
        print(" " * (num - i) + "*" * i)
    return

py(5)
