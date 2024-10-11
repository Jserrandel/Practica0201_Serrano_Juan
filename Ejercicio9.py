#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
Dinero = float(input("¿Cuanto quieres Ingresar?"))
Interes = float(input("¿Cuantos intereses tiene?"))
Años = int(input("¿Cuantos años lo mantendras?"))
print("El capital obtenido en la inversión es de " + str(round(Dinero* (Interes / 100 + 1) ** Años, 2)))