# Enunciado 1 – Registro de Productos con Arreglos Paralelos
# Crea tres arreglos paralelos para almacenar información de 4 productos: nombres, precios y cantidades en stock.
# Imprime un reporte que muestre cada producto con su precio y cantidad en una sola línea por producto.
# Además, calcula e imprime el precio total del inventario (precio × cantidad para todos).


products = ['Papel', 'Escobas', 'Recogedor', 'Shampoo']
prices = [3, 10, 7, 15]
stocks = [20, 5, 10, 8]
total_inventary = 0

print('='*25 + ' REPORTE DE INVENTARIO ' + '='*25)
for product, price, stock in zip(products, prices, stocks):

    total_inventary += (price * stock)
    print(f"Producto: {product:<10} | Precio: S/{price:<3} | Stock: {stock:<3} | Total: S/{price * stock}")

print('='*73)
print(' '*20 + f'VALOR TOTAL DEL INVENTARIO: S/{total_inventary}')
print('='*73)