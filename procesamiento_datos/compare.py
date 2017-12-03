
#cmp_to_key: function -> K
#funcion sorted necesita una key para determinar como ordenar
#reciba una funcion comparadora y retorna la key para usar en sorted
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

# compare_dates: array array -> bool
# compara dos arreglos segun las fechas que contengan
def compare_dates(array1, array2):
    a = array1[2].split("-"); c1 = 356 * int(a[0]) + 30 * int(a[1]) + int(a[2])
    b = array2[2].split("-"); c2 = 356 * int(b[0]) + 30 * int(b[1]) + int(b[2])
    return (c2 - c1) / max(abs(c2 - c1), 1)


# compare_ratings: array array -> bool
# compara dos arreglos segun los rating que contengan
def compare_ratings(array1, array2):
    c1 = int(array1[1])
    c2 = int(array2[1])
    return (c2 - c1) / max(abs(c2 - c1), 1)

# compare_id: array array -> bool
# compara dos arreglos segun el id del cliente
def compare_id(array1, array2):
    c1 = int(array1[0])
    c2 = int(array2[0])
    return (c2 - c1) / max(abs(c2 - c1), 1)