def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n-1)+recursive_nth_fibo(n-2)

def main():
    n = int(input("zadaj pozadovany pocet prvkov:"))
    seznam = []
    for i in range(n):
        seznam.append(recursive_nth_fibo(i))
    print(seznam)
    pass


if __name__ == "__main__":
    main()
