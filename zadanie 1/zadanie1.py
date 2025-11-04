#Damian Sadowski

#Łączenie list funkcją zip: https://realpython.com/ref/builtin-functions/zip/
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]
zipped = zip(names, scores)
print(list(zipped))

#Funkcja sqrt() z modułu math: https://docs.python.org/3/library/math.html
import math
number = 64
print("Pierwiastek z", number, "to", math.sqrt(number))

#Obsługa wyjątku ValueError: https://realpython.com/ref/builtin-exceptions/valueerror/
try:
    bad_number = int("abc")
except ValueError:
    print("Wartość nie może być przekonwertowana na liczbę całkowitą!")
    
