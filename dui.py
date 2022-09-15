# validación de DUI

"""
Crear un módulo para validación de DUI sin guion, que cumplirá las siguientes 
características: 
• El DUI debe contener 9 caracteres. 
• El DUI no puede contener espacios en blanco ni tampoco letras. 
• DUI válido, retorna “DUI valido” 
• DUI no válida, retorna el mensaje "DUI invalido". 

"""

def numeroDui ():

  Ndui=input("Ingrese numero de DUI : ")
  

  if len(Ndui)== 9:
    print(f"Numero de dui es: {Ndui} Es valido ")

  elif len(Ndui)>=10:
    print("Numero de dui Invalido * Debe contener 9 caracteres* ")

  else:
    len(Ndui)<= 8
    print("Numero de dui Invalido * Debe contener 9 caracteres* ")
   



  
      

  




 


