#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.
Horas = float(input("¿Cuantas horas has trabajado?"))
Pasta = float(input("¿Cuanto te pagan por hora?"))
Paga = Horas * Pasta
print("Te debemos", Paga, "euros")