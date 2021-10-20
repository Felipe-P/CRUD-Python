import time


n = 5
while n > 0:
    print(n)
    n -= 1

"""n = 5
while n > 0:
    print(n)
    n = n - 1
print('Despegue!!!')

n = int(input())
i = 0
while i < n:
    print(i ** 2)
    i += 1

while True:
    nombre = input("Ingrese un nombre: ")
    if nombre:
        break

password = "123456"
cont = 1
while True:
    passw = input("Ingrese una clave: ")
    if password == passw:
        print('Bienvenido al sistema')
        break
    elif passw != password:
        if cont < 3:
            cont += 1
            print('Clave incorrecta\n')
        else:
            break

n = 10
while True:
    print(n, end=' ')
    n -= 1
print('Terminado')
"""

# correo = 'prueba'
# clave = '123'
# repeat = True
# while repeat == True:
#     print('-' * 8 + 'Bienvenidos a Gmail' + '-' * 7)
#     print('Favor ingrese los siguientes datos')
#     print('-' * 34 + '\n')
#
#     cont = 1
#     intentos = 3
#     while True:
#         email = input('Email: ')
#         password = input('Clave: ')
#         print('\nValidando, por favor espere...')
#         if correo == email and clave == password:
#             print('Bienvenido de vuelta')
#             repeat = False
#             break
#         elif correo != email or clave != password:
#             if cont < intentos:
#                 print('El usuario o la clave son incorrectos\n')
#                 print('Intentos disponibles ', intentos - cont, '\n')
#                 cont += 1
#             else:
#                 print('Su cuenta ha sido bloqueada por 1 minuto!\n')
#                 time.sleep(4)
#                 repeat = True
#                 break
