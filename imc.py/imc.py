#Se declaran las variables
peso=0.0
altura=0.0
masa=0.0

#Mensaje de bienvenida 
print("Vamos a calcular tu Indice de Masa Corporal")
print("")

#Solicitar los datos del usuario
print("Por favor introduce los datos que se solicitan")
peso=float(input("Ingresa tu peso: "))
altura=float(input("Ingresa tu altura: "))

print("Espera un momento")
print("..")
print("...")
print("....")

#Calcular el IMC
Masa=peso/(altura*altura)

print(f"Tu IMC es: (Masa: .2f)")

#Evaluacion de los datos

if Masa < 18.5:
    print("Estas bajo de peso")
elif Masa >= 18.5 and Masa < 24.9:
    print("Tu peso es normal")
elif Masa >= 25 and Masa < 29.9:
    print("Tienes sobrepeso, debes cuidarte")
else:
    print("Tienes obesidad, debes cuidarte")