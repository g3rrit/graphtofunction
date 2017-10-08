import sys

def getValue(x):
    if  x >= 10 and x <= 20 or  x >= 300 and x <= 400:
        return x * x
    if  x < 10 and  x <= 8 or  x > 400:
        return x * 2
    if  x > 8 and x < 10 or  x > 20 and x < 300:
        return x + 2

def main():
    print(getValue(sys.argv[1])

if __name__ == "__main__":
    main()


