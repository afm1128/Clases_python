
 #operaciones
 #suma
a = 5
b = 2
c = a + b
print(c)

 

  #resta
a = 5
b = 2
c = a - b
print(c)
  
  
   #multiplicacion
a = 5
b = 2
c = a * b
print(c)
  
  
    #division
a = 5
b = 2
c = a / b
print(c)
  
      #division parte entera
a = 5
b = 2
c = a // b

print(c)
  
  #potencia
a = 5
b = 2
c = a ** b
print(c)

# string str
a = "hola mundo"
print(a)
# enero int
a = 5
# decimal float
a = 5.6
# booleano bool
x = True
y = False

# conversiones entre tipos de datos

# convertir de x a entero

a = '3'
y = int(a)
print(y)
print(type(y))

# convertir de x a decimal

a = 3
y = float(a)
print(y)
print(type(y))

# convertir de x a string

a = 3
y = str(a)
print(y)
print(type(y))
 
# concatenaciones 

a = 'hola'
b = 'mundo'
c = a +' ' + b
print(c)
 
 
a = 'hola'
b = a * 5
print(b)
 

# CAPTURAR POR PANTALLA
nombre = input('digite su nombre: ')
print('hola', nombre)

print(' digite su nombre: ')


# HUA que sume dos numeros e imprima su resultado

numero_uno = float(input('digite el numero uno: '))
numero_dos = float(input('digite el numero dos: '))
suma = numero_uno + numero_dos
print(suma)
print('La suma es: ', suma)
#forma usada (la que le gusta a el)
print(f'la suma es: {suma}') 


#HUA que lea un numero y te de el cuadrado
numero = float(input('digite el numero: '))
cuadrado = numero ** 2
print(f'el cuadrado es: {cuadrado}')

numero = float(input('digite el numero: '))
cuadrado = numero * numero
print(f'el cuadrado es: {cuadrado}')
#HUA que tome el valor de un producto le aplique el 20% de descuento imprima el valor del producto inicial, el valor con descuento y el valor ahorrado

valor_producto = int(input('digite el valor del producto: '))
descuento = valor_producto * 0.2
valor_final = valor_producto - descuento
print(f'el producto vale ${valor_producto: ,} el valor con descuento es ${valor_final: ,} el descuento fue de ${descuento: ,}')


#condicionales

#tabla de verdad

#tabla del and
# v and v = v
# v and f = f
# f and f = f
# f and v = f
# tabla del or
# v or v = v
# v or f = v
# f or v = v
# f or f = f

# tabla en python
# and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# negacion
print(not True)
print(not False)

#jerarquia de operaciones
# parentesis y llaves
# potencia y raices
# multiplicacion y division
# sumas y restas 
# sin nada de izquierda a derecha se resuelve

# jerarquia booleana
# parentesis y llaves
# tabla de verdad (de izquierda a derecha)

# mas de un condicional
print(True and False and Tue or False or True or True)
print(True and (False and Tue) or False or (True or True))

# Estructura if
if (x > 0):
    print('')
else:
    print('2')
#que dada la edad de una persona indique si es mayor o menor de edad

edad = int(input('digite la edad: '))
if edad >= 18:
    print()

nota = float(input('digite la nota: '))
if nota >= 3.0:
    print('aprobó la materia')
else:
    print('reprobó la materia')
    
nota = float(input('digite la nota: '))
if nota < 0 or nota > 5:
    print('no es una nota valida')   
elif nota >= 3.0:
    print('aprobó la materia')
else:
    print('reprobó la materia')

numero = float(input('digite la numero: '))
if numero > 0:
     print('el numero es positivo')
elif numero == 0 :
     print('el numero es 0')
else:
     print('el numero es negativo')
    
               


