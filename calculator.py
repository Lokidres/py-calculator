import math
import sys
import time
sys.set_int_max_str_digits(999999999) 

def toplama(x,y):
    return x+y

def cikarma(x,y):
    return x-y

def carpma(x,y):
    return x*y

def bolme(x,y):
    return x/y

def karekok(x):
    return math.sqrt(x)

def usalma(x,y):
    return x**y

def mod(x,y):
    return x%y

def faktoriyel(x):
    return math.factorial(x)

def logaritma(x, base):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def mutlak_deger(x):
    return abs(x)

def hipotenus(a, b):
    return math.hypot(a, b)

print("hesap makinesine hoşgeldiniz")
while True:
    try:
        secim = input("işlem seçiniz: 1-toplama 2-çıkarma 3-çarpma 4-bölme 5-karekök 6-üs alma 7-mod alma 8-faktoriyel 9-logaritma 10-sinüs 11-kosinüs 12-tanjant 13-mutlak değer 14-hipotenüs q-çıkış\nsecim: ")
        if secim == "1":
            sayi1 = int(input("ilk sayıyı giriniz: "))
            sayi2 = int(input("ikinci sayıyı giriniz: "))
            print("sonuc:",toplama(sayi1,sayi2))
        elif secim == "2":
            sayi1 = int(input("ilk sayıyı giriniz: "))
            sayi2 = int(input("ikinci sayıyı giriniz: "))
            print("sonuc:",cikarma(sayi1,sayi2))
        elif secim == "3":
            sayi1 = int(input("ilk sayıyı giriniz: "))
            sayi2 = int(input("ikinci sayıyı giriniz: "))
            print("sonuc:",carpma(sayi1,sayi2))
        elif secim == "4":
            sayi1 = int(input("ilk sayıyı giriniz: "))
            sayi2 = int(input("ikinci sayıyı giriniz: "))
            print("sonuc:",bolme(sayi1,sayi2))
        elif secim == "5":
            sayi1 = int(input("sayıyı giriniz: "))
            print("sonuc:",karekok(sayi1))
        elif secim == "6":
            sayi1 = int(input("taban sayıyı giriniz: "))
            sayi2 = int(input("üs sayıyı giriniz: "))
            print("sonuc:",usalma(sayi1,sayi2))
        elif secim == "7":
            sayi1 = int(input("ilk sayıyı giriniz: "))
            sayi2 = int(input("ikinci sayıyı giriniz: "))
            print("sonuc:",mod(sayi1,sayi2))
        elif secim == "8":
            sayi1 = int(input("sayıyı giriniz: "))
            print("sonuc:",faktoriyel(sayi1))
        elif secim == "9":
            sayi1 = int(input("sayıyı giriniz: "))
            base = int(input("taban sayıyı giriniz: "))
            print("sonuc:",logaritma(sayi1, base))
        elif secim == "10":
            sayi1 = int(input("açıyı giriniz: "))
            print("sonuc:",sin(sayi1))
        elif secim == "11":
            sayi1 = int(input("açıyı giriniz: "))
            print("sonuc:",cos(sayi1))
        elif secim == "12":
            sayi1 = int(input("açıyı giriniz: "))
            print("sonuc:",tan(sayi1))
        elif secim == "13":
            sayi1 = int(input("sayıyı giriniz: "))
            print("sonuc:",mutlak_deger(sayi1))
        elif secim == "14":
            sayi1 = int(input("ilk kenar uzunluğunu giriniz: "))
            sayi2 = int(input("ikinci kenar uzunluğunu giriniz: "))
            print("sonuc:",hipotenus(sayi1, sayi2))
        elif secim == "q":
            print("programdan çıkılıyor")
            time.sleep(1)
            break
    except Exception as e:
        print("hata olustu:", e)
  
