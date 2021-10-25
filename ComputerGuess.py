import random

def adivina(x):
    RandomNumber=random.randint(1,x)
    option= 0
    intentos = 5
    while option != RandomNumber and intentos > 0:
        option= int(input(f"Elige un número del 1 al {x} --> "))
        intentos=intentos-1

        if option > RandomNumber:
            print(f"el número que quiere adivinar es más chico. Intenta nuevamente con {intentos} intentos")

        elif option < RandomNumber:
            print(f"el número que quiere adivinar es más grande. Intenta nuevamente con {intentos} intentos")
    
    print(f"Felicidades! Adivinaste el número! \n El número que adivinaste fue el {RandomNumber} ")
 

print("\t\tBienvenido! \n\n")


adivina(10)

