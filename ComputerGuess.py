import random
from Estructura import *

def usuario_adivina(x, vidas):
   
    RandomNumber=random.randint(1,x)
    option= 0
    intentos = vidas
    while option != RandomNumber and intentos > 0:
        option= int(input(f"Elige un número del 1 al {x} --> "))
        intentos=intentos-1

        if option > RandomNumber:
            print(f"el número que quiere adivinar es más chico. Intenta nuevamente con {intentos} intentos")

        elif option < RandomNumber:
            print(f"el número que quiere adivinar es más grande. Intenta nuevamente con {intentos} intentos")
    
    if option== RandomNumber:
        print(f"Felicidades! Adivinaste el número! \n El número que adivinaste fue el {RandomNumber} ")
    elif intentos ==0:
        print(f"Lo siento. Se te acabaron los intentos. Perdiste :(")
 

def compu_adivina(x, vidas):
    print(f"Piensa un número del 1 al {x}.")
    pausa()
    low=1
    high=x
    lista_opciones=("a","b","c")
    intentos= vidas
    feedback = ""
    while feedback != "c" and intentos > 0:
        RandomNumber=random.randint(low,high)
        feedback= input(f"La computadora eligió el número --> {RandomNumber} <-- y le quedan {intentos} intentos. \n Con respecto al número pensado, es un valor muy alto (A), muy bajo (B), o es correcto (C)?\n ").lower()
        while feedback not in lista_opciones:
            feedback= input(f"El caracter ingresado es erróneo. Intentelo nuevamnete.\n (A) - Alto\n (B) - Bajo\n (C) - Correcto\n") 
                 
        
        if feedback == "a":
            high = RandomNumber -1
            intentos -=1
        elif feedback == "b":
            low = RandomNumber +1
            intentos -=1
    
    if feedback == "c":
        print(f"Increíblemente la máquina adivinó tu número pensado --> {RandomNumber}")
    elif intentos == 0:
        print(f"la computadora no pudo adivinar tu número en los intentos correspondientes.\n\n")
    

decision = ""
lista_dificultad = {"1":(10,3), "2":(100, 5), "3":(1000, 10), "4": (10, 3), "5":(100, 7), "6":(1000, 12)}
dificultad = ""

print("\t\tBienvenido! \n\n A qué quiere jugar?")
decision= input("\n (1) - Adivinar el número que piensa la compu.\n (2) - La compu adivina tu número.\n")
while not (decision == "1" or decision == "2"):
    decision=input(f"\n caracter erróneo. Elige bien la opción: ")

if decision == "1":
    dificultad = input("selecciona la dificultad:\n\n\t (1) - Fácil: tiene 3 intentos y el rango es de 1 al 10 \n\t (2) - Normal: tiene 5 vidas y el rango es de 1 al 100\n\t (3) - Dificl: tiene 10 vidas y el rango es de 1 al 1000")
    usuario_adivina(*lista_dificultad[dificultad])
elif decision== "2":
    
    dificultad = input("selecciona la dificultad:\n\n\t (4) - Fácil para la compu: tiene 3 intentos en un rango del 1 al 10 \n\t (5) - Normal para la compu: tiene 7 intentos en un rango del 1 al 100\n\t (6) - Dificil para la compu: tiene 12 intentos en un rango del 1 al 1000")
    compu_adivina(*lista_dificultad[dificultad])






