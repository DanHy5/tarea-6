# REGISTRO DE CLIENTES

print("ingrese sus datos a continuacion por favor.")

Nombre = input("Ingrese su nombre y apellido por favor: ")
Edad = int(input("Ingrese su edad: "))
Genero = str(input("Ingrese su genero:"))
Dia = str(input("Ingrese el dia: "))

if Genero == "femenino":
   hora = float(input("Ingrese la hora de su ingreso: "))
   if hora >= 22:
    print("Por promocion todas las damas pueden ingresar gratis apartir de las 22 horas.")
   else:
       print("La promocion lady's free solo aplica desde las 22 horas en adelante")

print("MENU DE BEBIDAS:")
print("Ingrese el numero del tipo de bebida   "
      "1.BEBIDAS CALIENTES "
      "2.CERVEZAS - AGUAS MINERALES")
menu = int(input("opcion: "))


if menu == 1:

    print('Escogio el menu de bebidas calientes.')
    print("seleccione una por medio de un numero:   "
          "1. Café  "
          "2. Café mediano  "
          "3. Café grande")
    cafe = int(input("Opcion "))

    costo_total = 0

    def sumar():
        global costo_total

        if cafe == 1:
            print('Cafe con un costo de $1.00')
            cafe1 = 1.00
            costo_total += cafe1

        elif cafe == 2:
             print('Cafe mediano con un costo de $1.50')
             cafe2 = 1.50
             costo_total += cafe2

        elif cafe == 3:
             print('Cafe grande con un costo de $2.00')
             cafe3 = 2.00
             costo_total += cafe3

    sumar()

    Repetir = "true"

    while Repetir == "true":
        Nuevo_pedido = str(input("Escoger nuevamente ? "))
        if Nuevo_pedido == "si":
            cafe = int(input("Opcion "))
        else:
            Repetir = "falso"
            cafe =cafe
            sumar()

    print("El valor total a pagar es: ", costo_total);

    print("Para realizar su pedido en el apartado de bebidas, se requiere una verificacion de su edad.")

elif menu == 2:

    if Edad >= 18:
        print("Su compra puede ser procesada")

        print('Escogio el menu de cervezas y aguas mineralizadas.')
        print("seleccione una por medio de un numero:   "
          "1. Agua  "
          "2. Cerveza Pilsener  "
          "3. Cerveza Club")
        bebida = int(input("Escoja una bebida por medio de uno de los numeros asignados: "))
        total1 = 0
        def suma():
          global total1
          if bebida == 1:
            print('agua con un costo de $1.00')
            bebida1 = 1.00
            total1 += bebida1

          elif bebida  == 2:
               print('Cerveca Pilsener con un costo de $2.50')
               bebida2 = 2.50
               total1 += bebida2

          elif bebida == 3:
              if Dia == "martes":
                  print('Cervesa Club con un costo de $3.00 , Mas Promocion Cigarrillo')
                  bebida3 = 3.00
                  total1 += bebida3
              else :
                  print('Cervesa Club con un costo de $3.00')
                  bebida3 = 3.00
                  total1 += bebida3

        suma()

        otro = "true"

        while otro == "true":
              Nueva_bebida = str(input("Escoger nuevamente ? "))
              if Nueva_bebida == "si":
                 bebida = int(input("Opcion "))
              else:
                otro = "falso"
                bebida = bebida
        suma()
        print("El valor total a pagar es: ", total1)
    else:
        print("Su compra no puede ser procesada por su edad, Gracias.")

print("La Musica en el Bar es a su eleccion.")

arr1 = ['BACHATAS: '"Eunel – (El Mismo)", "Joe – (Quiero)", "Romeo Santos – (Eres Mía)"]
arr2 = ['REGGAETON: '"(Yonaguni) - Bad Bunny", "(2/Catorce) - Rauw Alejandro", "(Bandido) - Myke Towers & Juhn"]
arr3 = ['ROCK: '"warcry - (quiero oirte)", "Kings of Leon - (Use somebody)", "Rata Blanca - Mujer Amante"]

for lista in arr1, arr2, arr3:
    print(lista)

musica = str(input("Ingrese el genero de musica: "))

if musica == "bachata":
    print("escoja una cancion: 1, 2, 3 ")
    b1 = int(input(""))
    if b1 == 1:
        print("reproduciendo : ", arr1[0])
        print("Puntuar la cancion"
              "La puntuacion va de 1 - 10")
        int(input(""))

    elif b1 == 2:
        print("reproduciendo: ", arr1[1])
        print("Puntuar la cancion"
              "La puntuacion va de 1 - 10")
        int(input(""))
    elif b1 == 3:
        print("reproduciendo: ", arr1[2])
        print("Puntuar la cancion"
              "La puntuacion va de 1 - 10")
        int(input(""))

if musica == "regaeton":
    print("escoja una cancion: 1, 2, 3 ")
    b2 = int(input(""))
    if b2 == 1:
        print("reproduciendo : ", arr2[0])
        print("Puntuar la cancion"
              "La puntuacion va de 1 - 10")
        int(input(""))
    elif b2 == 2:
        print("reproduciendo: ", arr2[1])
        print("Puntuar la cancion"
              "La puntuacion va de 1 - 10")
        int(input(""))
    elif b2 == 3:
        print("reproduciendo: ", arr2[2])
        print("Puntuar la cancion, "
              "La puntuacion va de 1 - 10")
        int(input(""))

if musica == "rock":
    print("escoja una cancion: 1, 2, 3 ")
    b3 = int(input(""))
    if b3 == 1:
        print("reproduciendo : ", arr3[0])
        print("Puntuar la cancion, "
              "La puntuacion va de 1 - 10")
        int(input(""))
    elif b3 == 2:
        print("reproduciendo: ", arr3[1])
        print("Puntuar la cancion, "
              "La puntuacion va de 1 - 10")
        int(input(""))
    elif b3 == 3:
        print("reproduciendo: ", arr3[2])
        print("Puntuar la cancion, "
              "La puntuacion va de 1 - 10")
        int(input(""))

agregar = str(input("Desea ingresar una nueva lista o cancion?"))
if agregar == "si":
          Nombre_cancion = str(input("Ingrese el nombre de la nueva cancion: "))
          print("Guardada la cancion y reproducioendo: ",Nombre_cancion)
else:
    agregar == "no"
    agregar = "no desea mas musica"
print(agregar)

print("CONTROL DE AFORO")

control = int(input("Empleado Ingrese la cantidad de personas que han ingresado al estableciemiento y no lo  "
                    "abandonan: "))
print(control ,"De un aforo maximo de 55 personas")
if control >=50:
    print("Se envia un mensaje al guardia que no permita mas el ingreso de las personas.")
elif control <=40:
    print("Se envia un mensaje al guardi informandole que el local cuenta con menos de 40 clientes")
else :

    print("este valor va a cambiar cuada vez que se ingrese un nuevo cliente")

print("En el caso de detectar anomalias en el comprotamiento de los clientes ingresar si u no respectivamente ")

comprotamiento = str(input("Buen o mal comportamiento? "))

if comprotamiento =="si":
    print("enviar al guardia a su lugar y hecharlo")
else:
    print("")



