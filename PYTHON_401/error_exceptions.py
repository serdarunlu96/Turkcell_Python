a=10
b=0

try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sıfır olmaz")

a=10
b="2"

try:
    print(a/b)
except TypeError:
    print("Sayı ve string problemi")

