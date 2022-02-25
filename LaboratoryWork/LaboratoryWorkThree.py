# Лабораторная работа № 3. Тема: Шифрование методом гаммирования.

# 2 Вариант: Тип датчика - Линейный конгруэнтный. Начальные данные а = 5, b = 7, m = 4096, Y0 = 4003.

a = 5
b = 7
m = 4096
Y0 = 4003

def Gamma(y):
    gamma_list = []
    for _ in range(8):
        y = (a * y + b) % m
        gamma_list.append(y)
    return gamma_list
 
def Encryption():
    gamma = Gamma(Y0)
    res = open("Result.txt", "w", encoding="utf-8")
    with open('Sourse.txt', 'r', encoding="utf-8") as f:
        r_int = ""
        r = ""
        while True:
            temp = f.read(8)
            if temp:
                for i, item in enumerate(temp):
                    r_int = r_int + " " + str(ord(item) ^ gamma[i])
                    r = r + " " + chr(ord(item) ^ gamma[i])
                    res.write(chr(ord(item) ^ gamma[i]))
 
            else:
                break
    print(r_int)
    res.close()
 
Encryption()
 
def Decryption():
    gamma = Gamma(Y0)
    res = open("NewResult.txt", "w", encoding="utf-8")
    with open('Result.txt', 'r', encoding="utf-8") as f:
        r_int = ""
        r = ""
        while True:
            temp = f.read(8)
            if temp:
                for i, item in enumerate(temp):
                    r_int = r_int + " " + str(ord(item) ^ gamma[i])
                    r = r + chr(ord(item) ^ gamma[i])
                    res.write(chr(ord(item) ^ gamma[i]))
            else:
                break
    print(r_int)
    res.close()
 
Decryption()