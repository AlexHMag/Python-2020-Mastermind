
dolar_euro = 0.91
libra_euro = 1.18

dinero = input("¿Que divisa quiere cambiar, dolares o libras (d/l)? ")
if dinero == "d":
    conversion = dolar_euro
    cantidad = float(input("Introduzca la cantidad: "))
    print("La cantidad en euros es: {}".format(cantidad * conversion))
if dinero == "l":
    conversion = libra_euro
    cantidad = float(input("Introduzca la cantidad: "))
    print("La cantidad en euros es: {}".format(cantidad * conversion))
if dinero != "d" and dinero != "l":
    print("No manejamos esa divisa")

