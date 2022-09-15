# validación la edad del usuario
"""
1. Crear un módulo para validación la edad del usuario (tomando como referencia el 
año 2022), que cumplirá las siguientes características: 
• La edad se calculará a partir de su fecha de nacimiento 
• La función debe recibir como parámetro el año de nacimiento 
• Si la edad es mayor o igual a 18 deberá retornar el mensaje "Eres mayor de 
edad". 
• Si la edad es menor a 18, retorna el mensaje "Eres menor de edad. 
• Si la edad resulta ser meno a cero o no es un valor numérico retornar “Fecha 
invalida” 
"""

def años():

    dia = int(input("Ingresa tu dia: "))
    mes = int(input("Ingresa tu mes: "))
    año = int(input("Ingresa tu año: "))


    edads = 2022 - año

    if (edads >= 18 ):
        print(f"Tu fecha de nacimiento es:  {dia} / {mes} / {año} ")
        print(f"Eres mayor de edad, tienes {edads} años")

    elif(edads >=1 or edads ==18 ):
        print(f"Tu fecha de nacimiento es:  {dia} / {mes} / {año} ")
        print(f"Eres menor de edad, tienes {edads} años")
    else:
        (edads == 0)
        print("Fecha Invalida")

   

      

    
