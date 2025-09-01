def leap_year():
   

    año_i=int(input("ingrese un año: "))
    año_f= float(año_i)
    año_div = año_f%4
    año_cent = año_f%400
    if año_div == 0 and año_cent == 0:
        print(f"El año {año_i} es bisiesto")

    else:

        print(f"El año {año_i} no es bisiesto")

