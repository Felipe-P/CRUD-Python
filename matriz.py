import numpy as np

# a = np.array([7, 5, 3, 1, 4, 2, 6])
# print(a)
#
b = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print(b)

# for i in range(0, len(b)):
#     fila = b[i]
#     for j in range(0, len(fila)):
#         print(fila[j])
#     print("\n")
#
# for i in range(3):
#     for j in range(4):
#         print(b[i][j], end="")
#         print()

# print(b[1])
# print("Elementos", b.size)
# print("Tamano", b.shape)
# print("Dimensiones", b.ndim)
#
# # Llena una matriz con ceros
# c = np.zeros(2)
# print(c)
# # llena una matriz con unos
# c = np.ones(2)
# print(c)
# # Deja vacia la matriz pero con los datos que hay en memoria
# c = np.empty(3)
# print(c)
# # llena una matriz con un rango
# c = np.arange(2, 9, 2)
# print(c)
# # Ordena el arreglo
# print(np.sort(a))


# # Operaciones de matrices
# data = np.array([[1, 2], [3, 4], [5, 6]])
# ones_row = np.array([[1, 1]])
# print(data + ones_row)
#
# a = np.array([[1, 2], [3, 4]])
# print(a.sum())
