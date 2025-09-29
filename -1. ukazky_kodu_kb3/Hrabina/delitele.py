def delitelnost(cislo): 
    for i in range (1, cislo):
        if cislo % i == 0:
            print(i)

cislo = int(input("zadej cislo "))
delitelnost(cislo)