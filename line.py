def line():
    

    coe_A = float(input("Ingrese el coeficiente A: "))
    coe_B = float(input("Ingrese el coeficiente B: "))
    coe_x1 =float(input("Ingrese el coeficiente X1: "))
    coe_x2 = float(input("Ingrese el coeficinte X2: "))

    print(f"El coeficiente A de su ecuación de la recta es: {coe_A}")
    print(f"El coeficiente B de su ecuación de la recta es: {coe_B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coe_x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coe_x2}")


    print("\nPara la siguiente ecuación:")

    print(f"\tY = {coe_A}X + {coe_B}") 


    
    Y1= (coe_A*coe_x1) + coe_B
    Y2= (coe_A*coe_x2) + coe_B
    
    P1= (coe_x1 , Y1)
    P2= (coe_x2 , Y2)

    print("\nDados los siguientes puntos:")
    print(f"\tP1 {P1}")
    print(f"\tP2 {P2}")

    X_dis = coe_x2 - coe_x1
    Y_dis = Y2 - Y1

    distancia = (X_dis**2 + Y_dis**2)**0.5

    print(f"\nLa distancia entre ellos es: {distancia}")

