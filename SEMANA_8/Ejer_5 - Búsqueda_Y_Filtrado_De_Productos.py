# Enunciado 5 – Búsqueda y Filtrado de Productos
# Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'.
# Implementa una función buscar_productos(lista, termino) que devuelva todos los productos
# cuyo nombre contenga el término de búsqueda (sin importar mayúsculas).
# Además, ordena los resultados por precio de menor a mayor.


def search_prodcut(list_products, term):
    save_product = []

    for key in list_products:
        if term.lower() in key['product_name'].lower():
            save_product.append(key)

    return sorted(save_product, key=lambda x: x['price'])

products = [
    {'product_name': 'Papel Higiénico', 'category': 'Aseo', 'price': 5},
    {'product_name': 'Pantalón', 'category': 'Prenda', 'price': 50},
    {'product_name': 'Shampoo', 'category': 'Aseo', 'price': 15},
    {'product_name': 'Manzana', 'category': 'Fruta', 'price':3},
    {'product_name': 'Plátano', 'category': 'Fruta', 'price': 2.5},
    {'product_name': 'Polo', 'category': 'Prenda', 'price': 25}
]

while True:
    search = input('Busca tu producto: ').strip()
    
    if search != "" and search.replace(" ", "").isalpha():
        break
    
    print("Error: Debe ingresar un texto válido (solo letras y espacios). Intente de nuevo.\n")

search_result = search_prodcut(products, search)
print('\n', '='*22, ' RESULTADOS DE BÚSQUEDA ', '='*22)
if len(search_result) == 0:
    print(' '*12, "No se encontró ningún producto.")
else:
    for product in search_result:
        print(' '*7, f"Producto: {product['product_name']:<16} | Cat: {product['category']:<7} | Precio: S/{product['price']:<5.2f}")
print('='*72)