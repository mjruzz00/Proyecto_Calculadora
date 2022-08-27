n1 = float(input("Introduce el primer número: ") )
n2 = float(input("Introduce el segundo número: ") )

opcion=0
while True:

    print("""
          Dime, ¿Qué quieres hacer?

          1)Sumar los dos valores
          2)Restar los dos valores
          3)Multiplicar los dos valores
          4)Dividir los dos valores
          5)Cambiar los dos valores
          6)Apagar calculadora
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
        n1= float(input("Introduce tu primer valor: ") )
        n2= float(input("Introduce tu segundo valor: ") )
    elif opcion == 6:
        break
    else:
        print("Opcioón Incorrecta")
        
    
