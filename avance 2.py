def pide_valor():
    n1 = float(input("Introduce el primer número: ") )
    n2 = float(input("Introduce el segundo número: ") )
    return n1,n2
n1,n2=pide_valor()

opcion=0
while True:

    print("""
          Dime, ¿Qué quieres hacer?
          1)Sumar los dos valores
          2)Restar los dos valores
          3)Multiplicar los dos valores
          4)Dividir los dos valores
          5)Porcentaje de dos valores
          6)Cambiar los dos valores
          7)Lista de datos
          8)Salir de la calculadora
          """)
    opcion = int(input("Escoge una opción: ") )

    if opcion == 1:
        print(" ")
        print("RESULTADO: la suma de" ,n1, "+" ,n2, "es igual a",n1+n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: la resta de" ,n1, "-" ,n2, "es igual a",n1-n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: el producto de" ,n1, "*" ,n2, "es igual a",n1*n2)
    elif opcion == 4:
        print(" ")
        print("RESULTADO: la división de" ,n1, "/" ,n2, "es igual a",n1/n2)
    elif opcion == 5:
        print(" ")
        print("RESULTADO: el porcentaje de" ,n1, "*" ,n2, "/100" , "es igual a",n1*n2/100)
    elif opcion == 6:
        n1,n2=pide_valor()
    elif opcion == 7:
        mylist = [n1,n2]
        print ("Lista Completa")
        print (mylist)
    elif opcion == 8:
        print("Salir de la calculadora")
        print(quit())
    else:
        print("Opción Incorrecta")
