# int / numero entero
numero=10

#float / decimal
float=13.14

#character / cadena de caracteres
character= "$"

#string / cadena de carateres 
cadena="hola como estas? bien chido"

#Mal uso de identificador 
palabra="123" #contraintuitivo
x="hola mundo" #no te dice nada sobre la representacion de la variable
num="120"#no abreviar, luego se hace bolas o codigo de spaguetti

#Mostrar resultados
print(f"Estos es un entero:{numero}")
print(f"Estos es un decimal:{float}")
print(f"Estos es un caracter:{character}")
print(f"Estos es una cadena:{cadena}")

  #Ejemplo de un banco
cuenta_bancaria = 2000000
retiro = 200
saldo_despues_del_retiro = cuenta_bancaria - retiro #se hace ya la operacion del retiro a tu cuenta
print(f"saldo en la cuenta:{cuenta_bancaria}")
print(f"saldo despues del retiro: {saldo_despues_del_retiro}")

#Como afectó tu retiro al saldo de tu cuenta
cuenta_bancaria=saldo_despues_del_retiro
print(f"saldo actual: {cuenta_bancaria}")