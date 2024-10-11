#Una panadería vende barras de pan a 3.49€ cada una. El pan que 
#no es el día tiene un descuento del 60%. Escribir un programa que comience
#leyendo el número de barras vendidas que no son del día. Después el 
#programa debe mostrar el precio habitual de una barra de pan, 
#el descuento que se le hace por no ser fresca y la ganancia final total.
Pandeayer = int(input("Numero de barras de pan de ayer: "))
Cuantovale = 3.49 
Descuento = 0.6
Precio = Pandeayer * Cuantovale * (1 - Descuento)
print("El pan de hoy cuesta --> " + str(Cuantovale) + "€")
print("El descuento de una barra de ayer es de --> " + str(Descuento * 100) + "%")
print("Tienes que pagar " + str(round(Precio, 2)) + "€")
#¿Una barra de pan a 3.49? ¿De donde sale la harina? ¿Del cielo o que?