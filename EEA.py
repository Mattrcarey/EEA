import sys


def EEA(x, y):
    if x == 0:
        return y, 0, 1
    gcd, a, b = EEA(y % x, x)
    return gcd, b - (y // x) * a, a


def main():
    inputs = sys.argv
    x = int(inputs[1])
    y = int(inputs[2])
    print(EEA(x,y))


if __name__ == "__main__":
    main()
