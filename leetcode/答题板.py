def foo(n):
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return foo(n * 2)
    else:
        return foo(n-5)

if __name__ == '__main__':
    for i in range(20,30):
        print(foo(i))