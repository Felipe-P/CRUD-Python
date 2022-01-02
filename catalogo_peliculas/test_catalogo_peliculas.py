from catalogo_peliculas.dominio.Pelicula import Pelicula
from catalogo_peliculas.servicio.catalogo_peliculas import CatalogoPeliculas as cp

menu = ['Agregar película', 'Listar películas', 'Eliminar archivo de pelíiculas', 'Salir']
opcion = None

while opcion != 4:
    try:
        print('Opciones:')
        for i in range(len(menu)):
            print(str(i + 1) + '.', menu[i])
        opcion = int(input('Seleccione una oopcion (1-4)'))

        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Saliendo del programa')
