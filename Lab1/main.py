
from datetime import date

# #Ex. 1
# print(3+11)
# print(1-3)
# print(3*3)
# print(4/6)
# print(2+1/5)
#
# #Ex. 2
# name = input("Wprowadz imie: ")
# print("Hi, " + name + "!")
#
# #Ex. 3
# first = int(input("Pierwsza liczba: "))
# second = int(input("Druga liczba: "))
#
# print(float(first+second))
#
# #Ex. 4
# print(sum(range(8, 81, 1)))
#
# #Ex. 5
# today = date.today()
# year = input("Podaj rok: ");
# month = input("Podaj miesiac: ")
# day = input("Podaj dzien: ")
# toCompare = date(int(year), int(month), int(day))
#
# print(today - toCompare)
#
#Ex. 6

sign = input("""
Wybierz działanie:
    + dodawanie
    - odejmowanie
    * mnożenie
    / dzielenie
    ^ potęgowanie
        
Type here: """)

first = int(input("Pierwsza liczba: "))
second = int(input("Druga liczba: "))

if(sign == "+"):
    print("Suma: " + str(first+second))
elif (sign == "-"):
    print("Różnica: " + str(first - second))
elif (sign == "*"):
    print("Iloczyn: " + str(first * second))
elif (sign == "/"):
    print("Iloraz: " + str(first / second))
elif (sign == "^"):
    print("Potęgowanie: " + str(first ** second))