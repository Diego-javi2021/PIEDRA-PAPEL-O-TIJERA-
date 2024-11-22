#importamos la libreria para generar números aleatorios (random).
import random

# Definición de las opciones a elegir, como variables.
PIEDRA = 1
PAPEL = 2
TIJERA = 3

#opcion para que imprima en pantalla  "¡Bienvenido al juego de Piedra, Papel o Tijera!, a continuacion se mostraran las opciones,"
print("¡Bienvenido al juego de Piedra, Papel o Tijera!, a continuacion se mostraran las opciones,")
   
print(f"{PIEDRA}: Piedra")
print(f"{PAPEL}: Papel")
print(f"{TIJERA}: Tijera")
# while(mientras) es un ciclo repetitivo que tiene repitiendo el codigo mientras una condicion sea verdadera (TRUE)
while True:
    jugador = int(input("Elige 1, 2 o 3: "))
    computadora = random.randint(1, 3)

    print(f"Tú elegiste {jugador}, la computadora eligió {computadora}")

    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == PIEDRA and computadora == TIJERA) or \
         (jugador == PAPEL and computadora == PIEDRA) or \
         (jugador == TIJERA and computadora == PAPEL):
        print("¡Ganaste!")
    else:
        print("Perdiste.")
#imprime en pantalla si deseamos jugar otra vez y nos permite responder opciones
    if input("¿Jugar otra vez? (si/no): ").lower() != "si":
     print("gracias por jugar :)")
        
        
    #fin del bucle 
     break